import rembg
from PIL import Image

input_path = 'portrait.jpg'
output_path = 'portrait.png'

print(f"Removing background from {input_path}...")
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_data = i.read()
        output_data = rembg.remove(input_data)
        o.write(output_data)
print("Done!")
