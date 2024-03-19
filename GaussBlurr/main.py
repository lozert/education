
from namefile import b
import numpy as np 
import matplotlib as mpl
import cv2
from matplotlib import pyplot as plt
import namefile 
import time 

start = time.time()

b = 1.5
low_gayss_matrix = np.array([[0.00000067 * b, 0.00002292 * b, 0.00019117 * b, 0.00038771 * b, 0.00019117 * b, 0.00002292 * b, 0.00000067 * b],
                            [0.00002292 * b, 0.00078633 * b, 0.00655965 * b, 0.01330373 * b, 0.00655965 * b, 0.00078633 * b, 0.00002292 * b],
                            [0.00019117 * b, 0.00655965 * b, 0.05472157 * b, 0.11098164 * b, 0.05472157 * b, 0.00655965 * b, 0.00019117 * b],
                            [0.00038771 * b, 0.01330373 * b, 0.11098164 * b, 0.22508352 * b, 0.11098164 * b, 0.01330373 * b, 0.00038771 * b],
                            [0.00019117 * b, 0.00655965 * b, 0.00655965 * b, 0.11098164 * b, 0.05472157 * b, 0.00655965 * b, 0.00019117 * b],
                            [0.00002292 * b, 0.00078633 * b, 0.00655965 * b, 0.01330373 * b, 0.00655965 * b, 0.00078633 * b, 0.00002292 * b],
                            [0.00000067 * b, 0.00002292 * b, 0.00019117 * b, 0.00038771 * b, 0.00019117 * b, 0.00002292 * b, 0.00000067 * b]])

img = cv2.imread(namefile.file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype('float32') / 255

color_img = img.shape[2]
height_img = img.shape[0]
width_img = img.shape[1]
height_filter = low_gayss_matrix.shape[0]
width_filter = low_gayss_matrix.shape[1]


new = np.zeros((height_img + int((width_filter+1) /2) , width_img + int((width_filter+1)/2) , color_img))
for i in range(color_img):
    new[ 1: -int(len(low_gayss_matrix)/2), 1: -int(len(low_gayss_matrix[0])/2), i] = img[:,:,i]


y = np.zeros((height_img, width_img, color_img))
count_color = 0

while(count_color < color_img):
    for i in range(int(height_filter / 2), new.shape[0] - int(height_filter / 2)):
        for j in range(int(width_filter / 2), new.shape[1] - int(width_filter / 2)):
            
            small_matrix = np.zeros((height_filter, width_filter))
            small_matrix = new[i-int(height_filter / 2):i + int((height_filter+1) / 2),  j-int(width_filter/2):j+ int((width_filter+1)/2), count_color]

            y[i- int(height_filter/2)][j- int(width_filter/2)][count_color] = (small_matrix * low_gayss_matrix).sum()

    count_color += 1
      

end = time.time() - start
print(end)

plt.imshow(y)
plt.show()


# PIL_img = T.ToPILImage()(y)



# # print(pic.shape)
# # # convert this torch tensor to PIL image 
# # PIL_img = T.ToPILImage()(pic)

# # # display result
# PIL_img.show()
