import customtkinter as ctk
from tkinter import messagebox
from main import SmartAttendance   # import your main system file

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class LoginPage:

    def __init__(self, root):

        self.root = root
        self.root.geometry("500x450")
        self.root.title("Login - Smart Attendance System")

        root.configure(fg_color="#e6ecff")

        # ===== Title =====
        title = ctk.CTkLabel(root,
                             text="Smart Attendance Login",
                             font=("Arial", 26, "bold"),
                             text_color="#1a237e")
        title.pack(pady=30)

        # ===== Frame =====
        frame = ctk.CTkFrame(root, width=350, height=300)
        frame.pack(pady=20)

        # ===== Username =====
        user_label = ctk.CTkLabel(frame, text="Username", font=("Arial", 14))
        user_label.pack(pady=10)

        self.username = ctk.CTkEntry(frame, width=250)
        self.username.pack()

        # ===== Password =====
        pass_label = ctk.CTkLabel(frame, text="Password", font=("Arial", 14))
        pass_label.pack(pady=10)

        self.password = ctk.CTkEntry(frame, width=250, show="*")
        self.password.pack()

        # ===== Login Button =====
        login_btn = ctk.CTkButton(frame,
                                  text="Login",
                                  width=200,
                                  command=self.login)
        login_btn.pack(pady=20)

        # ===== Exit Button =====
        exit_btn = ctk.CTkButton(root,
                                 text="Exit",
                                 fg_color="red",
                                 hover_color="#b71c1c",
                                 command=root.destroy)
        exit_btn.pack(pady=10)

    # ===== Login Function =====

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if username == "Admin123" and password == "Admin@123":

            messagebox.showinfo("Login", "Login Successful")

            self.root.destroy()

            root = ctk.CTk()
            app = SmartAttendance(root)
            root.mainloop()

        else:
            messagebox.showerror("Error", "Invalid Username or Password")


# ===== MAIN =====

if __name__ == "__main__":

    root = ctk.CTk()
    app = LoginPage(root)
    root.mainloop()