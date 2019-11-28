import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

averageImage = []
images = fits.open('speckledata.fits')[2].data

numberOfImages = len(images)
rowsCount = len(images[0])
columnCount = len(images[0][0])
Fourier = np.zeros((200, 200))

# iterate pixels on all positions
for pixelRow in range(rowsCount):
    for pixelColumn in range(columnCount):
        pixelSum = 0
        # summarize pixels in all pictures in {pixelRow} row and {pixelColumn} column
        for picture in images:
            pixelSum += picture[pixelRow][pixelColumn]
        averageImage.append(pixelSum / numberOfImages)  # append the average value of pixels

for picture in images:
    Fourier += np.abs(np.fft.fft2(picture))
fourierShift = np.fft.fftshift(Fourier)


plt.imshow(fourierShift, cmap='inferno', vmin=1, vmax=15000000)
plt.savefig('fourier.png')
plt.show()

reshapeImage = np.reshape(averageImage, (rowsCount, columnCount))
plt.imshow(reshapeImage, cmap='inferno', vmax=550, extent=(0, 512, 512, 0))
plt.savefig('mean.png')
plt.show()


rotaverImage = np.zeros((rowsCount, columnCount))
angle = []
a = 0
for i in range(100):
    a += 365 / 100
    angle.append(a)

for i in range(100):
    rotaverImage += ndimage.rotate(fourierShift, angle[i], reshape=False)
plt.imshow(rotaverImage, cmap='inferno', vmin=1, vmax=900000000)
plt.savefig('rotaver.png')
plt.show()


dividedImage = np.array(rotaverImage) / np.array(fourierShift)
plt.imshow(dividedImage, cmap='inferno')
plt.show()


maxFrequency = 25

# iterate pixels on all positions
for pixelRow in dividedImage:
    for pixel in pixelRow:
        if abs(pixel) < maxFrequency:
            pixel = 0

inverseFourier = np.fft.ifft2(dividedImage)
inverseFourierShift = np.fft.fftshift(inverseFourier)
plt.imshow(abs(inverseFourierShift), cmap='inferno', vmax=2.5)
plt.savefig('binary.png')
plt.show()
