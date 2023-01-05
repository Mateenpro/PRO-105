import os
import cv2


path = "pics"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif','webp']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)

print(count)
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 0.05, size)
for i in range(0,count-1):
    frame = cv2.imread(images[i])
    cv2.imshow("pics",images[i])
    out.write(frame)
cv2.waitKey(1000)
out.release()
print("done")    