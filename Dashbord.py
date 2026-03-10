import customtkinter as ctk
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1200x750")
        self.root.title("Smart Attendance Dashboard")

        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.create_csv()

        self.navbar()
        self.title()

        self.stats_frame = None
        self.chart_canvas = None

        self.attendance_stats()
        self.attendance_chart()
        self.last_entries()

        self.exit_button()

        self.auto_refresh()

    # ---------------- CSV ---------------- #

    def create_csv(self):

        if not os.path.exists("attendance.csv"):

            df = pd.DataFrame(columns=["ID","Roll","Name","Time","Date","Status"])
            df.to_csv("attendance.csv",index=False)

    # ---------------- Load Data ---------------- #

    def load_data(self):

        try:
            df = pd.read_csv("attendance.csv")

            if df.empty:
                return df

            today = datetime.now().strftime("%d/%m/%Y")

            today_data = df[df["Date"] == today]

            today_data = today_data.drop_duplicates(subset=["Roll"])

            return today_data

        except:
            return pd.DataFrame()

    # ---------------- Navbar ---------------- #

    def navbar(self):

        frame = ctk.CTkFrame(self.root,height=60,fg_color="#1a237e")
        frame.pack(fill="x")

        label = ctk.CTkLabel(frame,
        text="Smart Attendance Dashboard",
        font=("Arial",22,"bold"),
        text_color="white")

        label.pack(side="left",padx=20)

    # ---------------- Title ---------------- #

    def title(self):

        frame = ctk.CTkFrame(self.root,fg_color="transparent")
        frame.pack(pady=10)

        label = ctk.CTkLabel(frame,
        text="Today's Attendance",
        font=("Arial",28,"bold"))

        label.pack()

    # ---------------- Stats ---------------- #

    def attendance_stats(self):

        if self.stats_frame:
            self.stats_frame.destroy()

        self.stats_frame = ctk.CTkFrame(self.root,fg_color="transparent")
        self.stats_frame.pack(pady=10,padx=20,fill="x")

        df = self.load_data()

        if not df.empty:

            present = len(df[df["Status"]=="Present"])
            absent = len(df[df["Status"]=="Absent"])
            total = len(df)

        else:
            present = absent = total = 0

        stats = [
        ("Total",total,"#1e88e5"),
        ("Present",present,"#43a047"),
        ("Absent",absent,"#e53935")
        ]

        for i,(title,value,color) in enumerate(stats):

            card = ctk.CTkFrame(self.stats_frame,fg_color=color,corner_radius=15)
            card.grid(row=0,column=i,padx=20,pady=10,sticky="nsew")

            self.stats_frame.grid_columnconfigure(i,weight=1)

            ctk.CTkLabel(card,text=title,
            font=("Arial",15,"bold"),
            text_color="white").pack(pady=5)

            ctk.CTkLabel(card,text=str(value),
            font=("Arial",28,"bold"),
            text_color="white").pack(pady=10)

    # ---------------- Chart ---------------- #

    def attendance_chart(self):

        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()

        df = self.load_data()

        if not df.empty:

            present = len(df[df["Status"]=="Present"])
            absent = len(df[df["Status"]=="Absent"])

        else:
            present = 1
            absent = 1

        fig,ax = plt.subplots(figsize=(4,4))

        ax.pie([present,absent],
        labels=["Present","Absent"],
        autopct="%1.1f%%",
        colors=["green","red"])

        ax.set_title("Attendance Distribution")

        self.chart_canvas = FigureCanvasTkAgg(fig,master=self.root)
        self.chart_canvas.get_tk_widget().pack(pady=10)
        self.chart_canvas.draw()

    # ---------------- Last Entries ---------------- #

    def last_entries(self):

        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=10,padx=20,fill="x")

        df = pd.read_csv("attendance.csv")

        last = df.tail(5)

        tree = ttk.Treeview(frame,columns=list(last.columns),show="headings",height=5)

        for col in last.columns:

            tree.heading(col,text=col)
            tree.column(col,width=120,anchor="center")

        for _,row in last.iterrows():

            tree.insert("", "end", values=list(row))

        tree.pack(fill="x",pady=10)

    # ---------------- Auto Refresh ---------------- #

    def auto_refresh(self):

        if not self.running:
            return

        try:
            self.attendance_stats()
            self.attendance_chart()
        except:
            pass

        self.root.after(3000,self.auto_refresh)

    # ---------------- Exit ---------------- #

    def exit_button(self):

        btn = ctk.CTkButton(self.root,
        text="Exit",
        fg_color="#e53935",
        command=self.on_close)

        btn.pack(pady=10)

    # ---------------- Close ---------------- #

    def on_close(self):

        self.running=False
        self.root.destroy()


# ---------------- Main ---------------- #

if __name__=="__main__":

    root = ctk.CTk()
    app = Dashboard(root)
    root.mainloop()