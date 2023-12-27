const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const { PythonShell } = require('python-shell');
PythonShell.defaultPythonPath = 'C:/Program Files/Python311/python.exe';

const app = express();
const port = process.env.PORT || 3000;
const cors = require('cors');

app.use(express.json());
app.use(cors());
app.use(bodyParser.raw({ type: 'image/*', limit: '10mb' }));

// Endpoint untuk pemrosesan gambar
// Endpoint untuk pemrosesan gambar
app.post('/process_image', (req, res) => {
  const image = req.body.image;
  console.log('Received Image');

  // Memanggil skrip Python
  const options = {
      mode: 'json',
      pythonOptions: ['-u'],
      scriptPath: path.join(__dirname, 'scripts'),
      args: [JSON.stringify({ image })],
  };

  PythonShell.run('process_image.py', options, (err, results) => {
      if (err) {
          console.error(err);
          res.status(500).send('Internal Server Error');
          return;
      }

      const processedImage = results[0];
      console.log('Processed Image:', processedImage);

      // Kirim hasil pemrosesan kembali ke Flutter
      res.json({ result: processedImage });
  });
});


app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
