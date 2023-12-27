# skrip.py

from PIL import Image, ImageDraw
import pytesseract
import sys
import cv2
import numpy as np

def detect_and_contour_text(image_path, output_path):
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

        result = pytesseract.image_to_string(threshed, lang="ind")

        text_result = []
        for word in result.split("\n"):
            if "—" in word:
                word = word.replace("—", ":")
            if "”" in word:
                word = word.replace("”", ":")

            # Normalize NIK
            if "NIK" in word:
                nik_chars = word.split()
                if "D" in word:
                    word = word.replace("D", "0")
                if "?" in word:
                    word = word.replace("?", "7")

            text_result.append(word)

        contours, _ = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        draw = ImageDraw.Draw(Image.fromarray(img))  # Convert NumPy array to PIL Image
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)

        Image.fromarray(img).save(output_path)  # Convert back to NumPy array before saving
        # print(f"Kontur teks berhasil disimpan di: {output_path}")

        return text_result

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    input_image_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_image_path = "temp/result_image.jpg"

    if input_image_path is not None:
        result_text = detect_and_contour_text(input_image_path, output_image_path)
        # print(result_text)
        result_text_string = '\n'.join(result_text)
        
        print(result_text_string)
    else:
        print("Error: Harap berikan path gambar input.")
