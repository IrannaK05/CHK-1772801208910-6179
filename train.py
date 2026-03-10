
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1920x1080+0+0")
		self.root.title("Face Recongnition System")


		
		img3=Image.open(r"D:\Facial Recognition smart attendence system\Images\img3.jpg")       
		img3=img3.resize((1530,790),Image.BILINEAR)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=0,width=1530,height=790)
		title_lbl=Label(self.root,text="Train Data Set ",font=("times new roman",35,"bold"),background="red",foreground="white")
		title_lbl.place(x=0,y=0,width=1530,height=50)

        #button
                        
		std_img_btn=Image.open(r"D:\Facial Recognition smart attendence system\Images\img3.jpg")
		std_img_btn=std_img_btn.resize((180,180),Image.BILINEAR)
		self.std_img1=ImageTk.PhotoImage(std_img_btn)

		std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
		std_b1.place(x=650, y=200, width=180, height=180)

		std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
		std_b1_1.place(x=650, y=390, width=180, height=45)


		
		back=Button(self.root,command=self.Back,width=10,text="Back",font=("times new roman",15,"bold"),bg="white",foreground="red")
		back.place(x=1330,y=60)

	#define func for training data
	def train_classifier(self):
		data_dir=("Photo")
		path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

		faces=[]
		ids=[]	

		for image in path:
			img=Image.open(image).convert('L') #Converting to Gray scale
			imageNp=np.array(img, 'uint8')
			id=int(os.path.split(image)[1].split('.')[1])

			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Training", imageNp)
			cv2.waitKey(1)==13
		ids=np.array(ids)
		#=====Train the Classifier===
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces, ids)
		clf.write("test1.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("Result", "Training Data sets is completed!")	

	def Back(self):
		self.root.destroy()

if __name__=="__main__":
	root=Tk()
	obj=Train(root)
	root.mainloop()		