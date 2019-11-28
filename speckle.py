import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image, ImageDraw


averageImage = []
images = fits.open('speckledata.fits')[2].data

numberOfImages = len(images)
rowsCount = len(images[0])
columnCount = len(images[0][0])
Fourier = np.zeros((200,200))
# iterate pixels on all positions
for pixelRow in range(rowsCount):
    for pixelColumn in range(columnCount):
        pixelSum = 0
        # summarize pixels in all pictures in {pixelRow} row and {pixelColumn} column
        for picture in images:
            pixelSum += picture[pixelRow][pixelColumn]

        averageImage.append(pixelSum/numberOfImages)  # append the average value of pixels
x = np.fft.fft2(images[100])
for picture in images:
    Fourier += np.abs(np.fft.fft2(picture))
fourierShift = np.fft.fftshift(Fourier)
plt.imshow(fourierShift, cmap = 'inferno', vmin=1, vmax=15000000)
plt.savefig('fourier.png')
plt.show()
reshapeImage = np.reshape(averageImage, (rowsCount, columnCount))

plt.imshow(reshapeImage, cmap='inferno', vmax=550, extent=(0, 512, 512, 0))
plt.savefig('mean.png')
plt.show()
