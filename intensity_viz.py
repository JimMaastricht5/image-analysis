import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageEnhance, Image, ImageOps, ImageStat, ImageFilter, ImageChops

img = Image.open('/home/pi/birdclass/washout3.jpg')
img_np = np.array(img)
print(img_np.shape)  #rgb
red_np = img_np[:, :, 0]
green_np = img_np[:, :, 1]
blue_np = img_np[:, :, 2]
# plt.hist(img_np.ravel())  # Flatten the image array, measures all intensities
# plt.xlabel("Pixel Value: All")
# plt.ylabel("Frequency")
# plt.show()
#
# plt.hist(red_np.ravel())  # Flatten the image array, measures all intensities
# plt.xlabel("Pixel Value: Red")
# plt.ylabel("Frequency")
# plt.show()
#
# plt.hist(green_np.ravel())  # Flatten the image array, measures all intensities
# plt.xlabel("Pixel Value: Green")
# plt.ylabel("Frequency")
# plt.show()
#
# plt.hist(blue_np.ravel())  # Flatten the image array, measures all intensities
# plt.xlabel("Pixel Value: Blue")
# plt.ylabel("Frequency")
# plt.show()

# print(np.histogram(red_np, bins=20))
# # Calculate histogram with 20 bins
# counts, bins = np.histogram(red_np, bins=20)
#
# # Plot the histogram
# plt.bar(bins[:-1], counts)  # Plot using bin edges (excluding the rightmost edge)
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram of Random Data")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create box plot
# plt.boxplot(red_np)
# plt.xlabel("Data")
# plt.ylabel("Value")
# plt.title("Box Plot of the Data")
# plt.show()

ravg_intensity = np.mean(red_np)
gavg_intensity = np.mean(green_np)
bavg_intensity = np.mean(blue_np)
print(ravg_intensity, gavg_intensity, bavg_intensity)
print(np.mean(img_np))

# need to take some over exposed and underexposed photos for study
# need to create normalization
# resize to what and pad?
# need a count of photos by species and by month / day? Time of day?