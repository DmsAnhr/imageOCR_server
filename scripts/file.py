import base64
import cv2
import numpy as np
import json

def process_image(encoded_image):
    try:
        # Dekode gambar dari base64
        decoded_image = base64.b64decode(encoded_image)
        nparr = np.frombuffer(decoded_image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            raise Exception("Failed to decode image")

        # Ubah gambar menjadi hitam putih
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Encode gambar hasil pemrosesan ke base64
        _, encoded_processed_image = cv2.imencode('.png', gray_image)
        base64_processed_image = base64.b64encode(encoded_processed_image.tobytes()).decode('utf-8')

        return base64_processed_image

    except Exception as e:
        # Cetak pesan kesalahan dan hasil pemrosesan ke stdout
        error_message = {'error': f"Error processing image: {e}", 'result': None}
        print(json.dumps(error_message))
        return None

if __name__ == "__main__":
    # Contoh data input untuk pengujian
    example_input = {"image": "/9j/4AAQSkZJRgABAQEAYABgAAD/4RByRXhpZgAATU0AKgAAAAgAAwESAAMAAAABAAEAAIdpAAQAAAABAAAIPuocAAcAAAgMAAAAMgAAAAAc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACkAAABwAAAAQwMjIw6hwABwAACAwAAAhcAAAAABzqAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/4QjdaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIi8+PC94OnhtcG1ldGE+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg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"}

    try:
        # Membaca data JSON dari input contoh
        encoded_image = example_input.get('image')  

        # Proses gambar
        if encoded_image:
            processed_image = process_image(encoded_image)
            if processed_image is not None:
                # Kembalikan hasil pemrosesan sebagai JSON
                result = {'result': processed_image}
                print(json.dumps(result))
            else:
                # Tangani kesalahan jika ada
                sys.exit(1)
        else:
            # Tangani kesalahan jika tidak ada data gambar
            error_message = {'error': 'Invalid input data or missing image field', 'result': None}
            print(json.dumps(error_message))
            sys.exit(1)
    except Exception as e:
        # Tangani kesalahan selama proses
        error_message = {'error': f"Error processing image: {e}", 'result': None}
        print(json.dumps(error_message))
        sys.exit(1)
