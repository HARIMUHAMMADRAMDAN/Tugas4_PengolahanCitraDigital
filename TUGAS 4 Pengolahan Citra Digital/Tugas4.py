import numpy as np
import imageio.v2 as imageio  
from scipy.ndimage import histogram

def histogram_equalization(image):
    
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()  
    cdf_normalized = cdf / cdf.max()  

    
    new_values = np.floor(255 * cdf_normalized).astype('uint8')


    equalized_image = new_values[image]
    return equalized_image


input_image_path = 'image.jpg'  
output_image_path = 'hasil_equalized_image.jpg'

image = imageio.imread(input_image_path)
if image.ndim == 3:  
    image = np.mean(image, axis=2).astype('uint8')


equalized_image = histogram_equalization(image)


imageio.imwrite(output_image_path, equalized_image)

print("Ekualisasi histogram selesai. Citra disimpan sebagai", output_image_path)
