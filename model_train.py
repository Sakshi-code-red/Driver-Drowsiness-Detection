import cv2
import os

main_folder_path=(r"C:\Users\User\Desktop\Driver Drowsiness\DDD_project_dataset\train")   
main_folder_name=os.path.basename(main_folder_path)
print("folder Name:",main_folder_name)

main_folder_items=os.listdir(main_folder_path) 
print("item inside folder :",main_folder_items)

map = {'Open_Eyes':0,'Closed_Eyes':1}

x=[]  
y=[]

for i in range(0,len(main_folder_items)):
	img_folder_path=os.path.join(main_folder_path,main_folder_items[i])  
	img_folder_label=os.path.basename(img_folder_path) 
	print("folder_label:",img_folder_label)
	img_inside_folder=os.listdir(img_folder_path)  
	print("inside folder:",img_inside_folder)
	
	
	for j in range(0,len(img_inside_folder)): 
		img_path=os.path.join(img_folder_path,img_inside_folder[j])
		img=cv2.imread(img_path)
		img = cv2.resize(img,(50, 50))
		img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
		img=img.flatten()
		x.append(img)
		y.append(map[img_folder_label])	

import numpy as np
x=np.array(x)
y=np.array(y)

from sklearn.neighbors  import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1)
    
model.fit(x,y)

y_predicted=model.predict(x)

print("model selected successfully")
print("ML predicted y :",y_predicted)
print('model trained')

acc=model.score(x,y)
print('model performance',acc)

import joblib as jb
jb.dump(model,'ddd.pkl')
print('model saved successfully')