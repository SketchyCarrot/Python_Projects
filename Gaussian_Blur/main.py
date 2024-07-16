from skimage import io, filters
from matplotlib import pyplot

image = io.imread("images/glWla8v.png")
gaussian_blur = filters.gaussian(image, sigma=2)

pyplot.imshow(gaussian_blur)