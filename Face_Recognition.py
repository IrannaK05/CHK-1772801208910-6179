import customtkinter as ctk
from PIL import Image
import cv2
import os
import mysql.connector
from datetime import datetime
import numpy as np

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Face_Recognition_UI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x750")
        self.root.title("Face Recognition System")
        self.root.configure(fg_color="#e6ecff")  # Background color

        self.setup_navbar()
        self.setup_title()
        self.setup_cards()

        # Back button
        ctk.CTkButton(self.root, text="Back", fg_color="#e53935", hover_color="#b71c1c",
                       font=("Arial", 15, "bold"), width=150, command=self.root.destroy).pack(side="bottom", pady=20)

    # ================= NAVBAR =================
    def setup_navbar(self):
        navbar = ctk.CTkFrame(self.root, height=60, fg_color="#1a237e")
        navbar.pack(fill="x")

        logo_img = ctk.CTkImage(
            Image.open(r"D:\Facial Recognition smart attendence system\Images\img3.jpg"),
            size=(40, 40)
        )

        logo = ctk.CTkLabel(navbar, image=logo_img, text="")
        logo.pack(side="left", padx=10)

        title = ctk.CTkLabel(navbar, text="Smart Attendance System",
                             font=("Arial", 20, "bold"), text_color="white")
        title.pack(side="left")

        home_btn = ctk.CTkButton(navbar, text="Home", width=80,
                                 fg_color="transparent", hover_color="#3949ab")
        home_btn.pack(side="right", padx=10)

        help_btn = ctk.CTkButton(navbar, text="Help", width=80,
                                 fg_color="transparent", hover_color="#3949ab")
        help_btn.pack(side="right", padx=10)

        login_btn = ctk.CTkButton(navbar, text="Login", width=80,
                                  fg_color="transparent", hover_color="#3949ab")
        login_btn.pack(side="right", padx=10)

    # ================= Title =================
    def setup_title(self):
        title = ctk.CTkLabel(self.root, text="Face Recognition System",
                             font=("Arial", 30, "bold"), text_color="#ffffff", fg_color="#1a237e")
        title.pack(fill="x", pady=(10, 20))

    # ================= Cards =================
    def setup_cards(self):
        card_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        card_frame.pack(pady=20, padx=20, fill="both", expand=True)
        card_frame.grid_columnconfigure(0, weight=1)  # Only one card

        # Only Face Detector card
        self.create_card(card_frame, 0, 0, "Face Detector", "Start the face detection system",
                         r"D:\Facial Recognition smart attendence system\Images\fd.jpg", self.face_recog)

    def create_card(self, parent, row, col, title, desc, img_path, command=None):
        img = ctk.CTkImage(Image.open(img_path), size=(120, 120))

        card = ctk.CTkFrame(parent, corner_radius=20, fg_color="#e3f2fd",
                             border_width=2, border_color="#c5cae9")
        card.grid(row=row, column=col, padx=30, pady=25, sticky="nsew")

        ctk.CTkLabel(card, image=img, text="").pack(pady=15)
        ctk.CTkLabel(card, text=title, font=("Arial", 18, "bold"), text_color="#1a237e").pack(pady=5)
        ctk.CTkLabel(card, text=desc, wraplength=200, justify="center", text_color="#333").pack(pady=5)
        ctk.CTkButton(card, text="Start", fg_color="#3949ab", hover_color="#1a237e",
                       font=("Arial", 15, "bold"), command=command).pack(pady=10)

    # ================= FACE RECOGNITION =================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root",
                                               password="IrannaDK@0504", database="student_database")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT Student_id, Roll, Name FROM student_details WHERE Student_id=%s", (id,))
                result = my_cursor.fetchone()
                if result:
                    i, r, n = map(str, result)
                else:
                    i = r = n = "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img

        def recognize(img, clf, faceCascade):
            return draw_boundary(img, faceCascade, 1.1, 10, clf)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("test2.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Enter key to exit
                break
        video_cap.release()
        cv2.destroyAllWindows()

    # ================= MARK ATTENDANCE =================
    def mark_attendance(self, i, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},Present")


# ================= MAIN =================
if __name__ == "__main__":
    root = ctk.CTk()
    app = Face_Recognition_UI(root)
    root.mainloop()