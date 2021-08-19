from PIL import Image
import os

img_dir = input('Enter Directory Path: ').replace('"', '')

try:
    for img_file in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_file)
        if os.path.isfile(img_path):
            new_img_path = os.path.join(img_dir, os.path.splitext(img_path)[0] + '.png')
            new_img_file = Image.open(img_path).convert('RGB') # Convert to 24Bit
            new_img_file.save(new_img_path)

except Exception as exception:   
    print('Error : %s!' % str(exception))
