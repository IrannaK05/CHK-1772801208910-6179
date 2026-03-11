import customtkinter as ctk
from Student import Student
from PIL import Image
from Dashbord import Dashboard
import os

# Import other modules
from Face_Recognition import Face_Recognition_UI
from attendance import Attendance
from Train import Train_UI

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SmartAttendance:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1300x750")
        self.root.title("Smart Attendance System")

        root.configure(fg_color="#e6ecff")

        # ================= NAVBAR =================

        navbar = ctk.CTkFrame(root, height=60, fg_color="#1a237e")
        navbar.pack(fill="x")

        logo_img = ctk.CTkImage(
            Image.open(r"D:\Facial Recognition smart attendence system\Images\img3.jpg"),
            size=(40, 40)
        )

        logo = ctk.CTkLabel(navbar, image=logo_img, text="")
        logo.pack(side="left", padx=10)

        title = ctk.CTkLabel(
            navbar,
            text="Smart Attendance System",
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        title.pack(side="left")

        home = ctk.CTkButton(navbar, text="Home", width=80,
                             fg_color="transparent",
                             hover_color="#3949ab")
        home.pack(side="right", padx=10)

        help_btn = ctk.CTkButton(navbar, text="Help", width=80,
                                 fg_color="transparent",
                                 hover_color="#3949ab")
        help_btn.pack(side="right", padx=10)

        login = ctk.CTkButton(navbar, text="Login", width=80,
                              fg_color="transparent",
                              hover_color="#3949ab")
        login.pack(side="right", padx=10)

        # ================= HERO =================

        hero = ctk.CTkFrame(root, fg_color="transparent")
        hero.pack(pady=20)

        circle_img = ctk.CTkImage(
            Image.open(r"D:\Facial Recognition smart attendence system\Images\main.jpg"),
            size=(120, 120)
        )

        img_label = ctk.CTkLabel(hero, image=circle_img, text="")
        img_label.pack()

        heading = ctk.CTkLabel(
            hero,
            text="Smart Attendance System",
            font=("Arial", 30, "bold"),
            text_color="#1a237e"
        )
        heading.pack(pady=5)

        desc = ctk.CTkLabel(
            hero,
            text="Face Recognition Based Smart Attendance System",
            font=("Arial", 14),
            text_color="#333333"
        )
        desc.pack()

        # ================= CARDS =================

        card_frame = ctk.CTkFrame(root, fg_color="transparent")
        card_frame.pack(pady=20, padx=20, fill="both", expand=True)

        card_frame.grid_columnconfigure((0, 1, 2), weight=1)

        def create_card(row, col, title, desc, img_path, color, command=None):

            img = ctk.CTkImage(Image.open(img_path), size=(60, 60))

            card = ctk.CTkFrame(
                card_frame,
                corner_radius=20,
                fg_color=color,
                border_width=2,
                border_color="#c5cae9"
            )

            card.grid(row=row, column=col, padx=30, pady=25, sticky="nsew")

            icon = ctk.CTkLabel(card, image=img, text="")
            icon.pack(pady=15)

            btn = ctk.CTkButton(
                card,
                text=title,
                fg_color="#3949ab",
                hover_color="#1a237e",
                font=("Arial", 15, "bold"),
                width=200,
                command=command
            )
            btn.pack(pady=5)

            description = ctk.CTkLabel(
                card,
                text=desc,
                wraplength=220,
                justify="center",
                text_color="#333"
            )
            description.pack(pady=10)

        # ===== CARDS =====

        create_card(0, 0, "Student Details",
                    "Add and manage student records.",
                    r"D:\Facial Recognition smart attendence system\Images\sd.png",
                    "#e3f2fd",
                    command=lambda: self.open_page(Student))

        create_card(0, 1, "Face Detector",
                    "Detect and recognize student faces.",
                    r"D:\Facial Recognition smart attendence system\Images\fd.jpg",
                    "#e3f2fd",
                    command=lambda: self.open_page(Face_Recognition_UI))

        create_card(0, 2, "Attendance",
                    "Mark attendance using face recognition.",
                    r"D:\Facial Recognition smart attendence system\Images\images.jpg",
                    "#e3f2fd",
                    command=lambda: self.open_page(Attendance))

        create_card(1, 0, "Train Data",
                    "Train dataset for recognition system.",
                    r"D:\Facial Recognition smart attendence system\Images\train.jpg",
                    "#e3f2fd",
                    command=lambda: self.open_page(Train_UI))

        create_card(1, 1, "Photos",
                    "Manage captured student photos.",
                    r"D:\Facial Recognition smart attendence system\Images\img3.jpg",
                    "#e3f2fd",
                    command=self.open_img)

        create_card(1, 2, "Dashboard",
                    "Show percentage of student attendance.",
                    r"D:\Facial Recognition smart attendence system\Images\dash.jpg",
                    "#e3f2fd",
                    command=lambda: self.open_page(SmartAttendanceDashboard))

        # ================= EXIT =================

        exit_btn = ctk.CTkButton(
            root,
            text="Exit",
            fg_color="#e53935",
            hover_color="#b71c1c",
            font=("Arial", 15, "bold"),
            width=200,
            command=root.destroy
        )

        exit_btn.pack(pady=20)

    # ================= UNIVERSAL PAGE OPEN FUNCTION =================

    def open_page(self, page_class):

        new_window = ctk.CTkToplevel(self.root)

        new_window.lift()
        new_window.focus()
        new_window.attributes("-topmost", True)

        new_window.after(200, lambda: new_window.attributes("-topmost", False))

        page_class(new_window)

    # ================= OPEN PHOTO FOLDER =================

    def open_img(self):

        path = r"D:\Iranna\Facial Recognition smart attendence system\Photo"

        if os.path.exists(path):
            os.startfile(path)
        else:
            print("Photos folder not found")


# ================= MAIN =================

if __name__ == "__main__":
    root = ctk.CTk()
    app = SmartAttendance(root)
    root.mainloop()