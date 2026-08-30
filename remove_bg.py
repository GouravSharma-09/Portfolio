import rembg
from PIL import Image

input_path = 'portrait.png'
output_path = 'portrait.png'

print(f"Removing background from {input_path}...")
with open(input_path, 'rb') as i:
    input_data = i.read()

output_data = rembg.remove(input_data)

with open(output_path, 'wb') as o:
    o.write(output_data)
print("Done!")
