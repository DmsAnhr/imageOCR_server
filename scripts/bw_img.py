from PIL import Image
import sys

def convert_to_black_and_white(image_path, output_path):
    try:
        # Buka gambar dari path yang diberikan
        image = Image.open(image_path)
        
        # Ubah ke hitam putih
        black_and_white_image = image.convert('L')

        # Simpan gambar hasil ke path yang diberikan
        black_and_white_image.save(output_path)

        print(f"Image converted to black and white and saved at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Menerima path gambar input dan output dari command line
    input_image_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_image_path = "temp/result_image.jpg"

    if input_image_path is not None:
        convert_to_black_and_white(input_image_path, output_image_path)
    else:
        print("Error: Harap berikan path gambar input dan output.")
