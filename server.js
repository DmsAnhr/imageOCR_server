const express = require('express');
const multer = require('multer');
const { spawn, exec } = require('child_process');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post('/ocr', upload.single('photo'), (req, res) => {
  const pythonScriptPath = 'D:/Kampus/SMT_5/TA/serverML/scripts/ocr_img.py';

  const tempImagePath = path.join(__dirname, 'temp', 'uploaded_image.jpg');
  const photoBuffer = req.file.buffer;

  require('fs').writeFileSync(tempImagePath, photoBuffer);

  // Jalankan skrip Python dengan child_process dan kirim path gambar sebagai argumen
  const pythonProcess = exec(`python ${pythonScriptPath} ${tempImagePath}`, (error, stdout, stderr) => {
    
    console.log('Recognize Text...');
    console.log('stdout:', stdout);
    console.log('stderr:', (stderr != "") ? stderr : "No Error");
    
    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).send('Internal Server Error');
    }

    res.send(stdout);
  });
});

app.post('/bw', upload.single('photo'), (req, res) => {
  const pythonScriptPath = 'D:/Kampus/SMT_5/TA/serverML/scripts/bw_img.py';

  const tempImagePath = path.join(__dirname, 'temp', 'uploaded_image.jpg');
  const photoBuffer = req.file.buffer;

  require('fs').writeFileSync(tempImagePath, photoBuffer);

  // Jalankan skrip Python dengan child_process dan kirim path gambar sebagai argumen
  const pythonProcess = exec(`python ${pythonScriptPath} ${tempImagePath}`, (error, stdout, stderr) => {
    
    console.log('Convert Black & White...');
    console.log('stdout:', stdout);
    console.log('stderr:', (stderr != "") ? stderr : "No Error");

    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).send('Internal Server Error');
    }

    const resultImagePath = path.join(__dirname, 'temp', 'result_image.jpg');
    const resultImageBuffer = require('fs').readFileSync(resultImagePath);

    // Kirim gambar hasil sebagai respons
    res.writeHead(200, {
      'Content-Type': 'image/jpeg',
      'Content-Length': resultImageBuffer.length
    });
    res.end(resultImageBuffer, 'binary');
    // fs.unlinkSync(tempImagePath);
    fs.unlinkSync(resultImagePath);
  });
});

// app.post('/process_image', upload.single('image'), (req, res) => {
//   if (!req.file) {
//     return res.status(400).json({ error: 'No file provided' });
//   }

//   console.log('ok');

//   // Simpan gambar ke file sementara
//   const filePath = path.join(__dirname, 'temp', 'temp.jpg');
//   fs.writeFileSync(filePath, req.file.buffer);

//   // Proses gambar menggunakan skrip Python
//   const pythonScriptPath = path.join(__dirname, 'scripts', 'process_image.py');
//   const pythonProcess = spawn('python', [pythonScriptPath, filePath]);

//   pythonProcess.on('close', (code) => {
//     if (code !== 0) {
//       console.error(`Image processing failed with code ${code}`);
//       return res.status(500).json({ error: 'Image processing failed' });
//     }

//     // Baca hasil gambar yang telah diproses
//     const processedImagePath = path.join(__dirname, 'temp', 'processed.jpg');
//     const processedImage = fs.readFileSync(processedImagePath);

//     // Kirim hasil gambar ke aplikasi Flutter
//     res.send(processedImage);

//     // Hapus file sementara
//     fs.unlinkSync(filePath);
//     fs.unlinkSync(processedImagePath);
//   });
// });

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
