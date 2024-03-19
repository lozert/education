
import numpy as np 
import matplotlib as mpl
import cv2
from matplotlib import pyplot as plt
import namefile 

low_gayss_matrix = np.array([[0.00000067, 0.00002292, 0.00019117, 0.00038771, 0.00019117, 0.00002292, 0.00000067],
                        [0.00002292, 0.00078633, 0.00655965, 0.01330373, 0.00655965, 0.00078633, 0.00002292],
                        [0.00019117, 0.00655965, 0.05472157, 0.11098164, 0.05472157, 0.00655965, 0.00019117],
                        [0.00038771, 0.01330373, 0.11098164, 0.22508352, 0.11098164, 0.01330373, 0.00038771],
                        [0.00019117, 0.00655965, 0.00655965, 0.11098164, 0.05472157, 0.00655965, 0.00019117],
                        [0.00002292, 0.00078633, 0.00655965, 0.01330373, 0.00655965, 0.00078633, 0.00002292],
                        [0.00000067, 0.00002292, 0.00019117, 0.00038771, 0.00019117, 0.00002292, 0.00000067]])

img = cv2.imread(namefile.file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype('float32') / 255
# low_gayss_matrix = np.array([[0.4, 0.3, 0.2],
#                              [0.4, 0.3, 0.2],
#                              [0.4, 0.3, 0.2]])


# img = np.array([[[1, 2, 3, 1, 1, 1, 1],
#                 [2, 3, 1, 1, 1, 1, 1],
#                 [1, 4, 5, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1]],
                
#                 [[1, 2, 3, 1, 1, 1, 1],
#                 [2, 3, 1, 1, 1, 1, 1],
#                 [1, 4, 5, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1]]])

print(img.shape)

color_img = img.shape[2]
height_img = img.shape[0]
width_img = img.shape[1]

height_filter = low_gayss_matrix.shape[0]
width_filter = low_gayss_matrix.shape[1]

print(low_gayss_matrix.shape)
print(color_img)
print(height_img)
print(width_img)



new = np.zeros((height_img + int((width_filter+1) /2) , width_img + int((width_filter+1)/2) , color_img))
print(new.shape)
for i in range(color_img):
    new[ 1: -int(len(low_gayss_matrix)/2), 1: -int(len(low_gayss_matrix[0])/2), i] = img[:,:,i]


y = np.zeros((height_img, width_img, color_img))
print(y.shape)
count_color = 0



def sumMatrix(small_matrix): # Свёртка 
    summ = 0

    for i in range(len(small_matrix)):
        for j in range(len(small_matrix[0])):
            # print(f"SM {small_matrix[i][j]} * LGM {low_gayss_matrix[i][j]} \n")
            summ += float(small_matrix[i][j]) * float(low_gayss_matrix[i][j])
    
    return summ

while(count_color < color_img):
    for i in range(int(height_filter / 2), new.shape[0] - int(height_filter / 2)):
        for j in range(int(width_filter / 2), new.shape[1] - int(width_filter / 2)):
            
            small_matrix = np.zeros((height_filter, width_filter))
          
            small_matrix = new[i-int(height_filter / 2):i + int((height_filter+1) / 2),  j-int(width_filter/2):j+ int((width_filter+1)/2), count_color]
            y[i- int(height_filter/2)][j- int(width_filter/2)][count_color] = sumMatrix(small_matrix)

    count_color += 1
      

print(y)

plt.imshow(y)
plt.show()

# PIL_img = T.ToPILImage()(y)



# # print(pic.shape)
# # # convert this torch tensor to PIL image 
# # PIL_img = T.ToPILImage()(pic)

# # # display result
# PIL_img.show()
