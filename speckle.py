
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np

a = 0
image_data = []
data = fits.open('speckledata.fits')[2].data

for i in range(len(data[0])):
    for j in range(len(data[0][i])):
        a = 0
        for k in range(len(data)):
            a += data[k][i][j]
        image_data.append(a/len(data))
reshape_data = np.reshape(image_data, (len(data[0]), len(data[0][0])))

plt.imshow(reshape_data, cmap='inferno', vmax=550)

plt.savefig('mean.png')
plt.show()
