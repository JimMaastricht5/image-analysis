import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageEnhance, Image, ImageOps, ImageStat, ImageFilter, ImageChops

img = Image.open('/home/pi/birdclass/0.jpg')
# Assuming you have your image data in a NumPy array (e.g., image)
# plt.imshow(img, cmap='hot')  # 'hot' is a colormap for heatmaps
# plt.colorbar()  # Add a colorbar to interpret value-color mapping
# plt.show()

img_np = np.array(img)
plt.hist(img_np.ravel())  # Flatten the image array
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
