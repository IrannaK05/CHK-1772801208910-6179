# Smart Attendance System using Face Recognition ## 
📌 Project Overview The 
**Smart Attendance System** is an AI-based application that automatically records student attendance using **face recognition technology**. The system detects and recognizes student faces through a camera and stores attendance records in a database. 
This project eliminates manual attendance, reduces proxy attendance, and provides real-time attendance analytics through a dashboard. 
The system is developed using **Python**, **computer vision**, and a **database management system**. 

--- ## 🚀 Features * 👤 Student registration system *
 📷 Face dataset generation using camera
  * 🧠 Face recognition using machine learning *
   📝 Automatic attendance marking *
    📊 Attendance dashboard with statistics * 
    🗄 Database storage for student and attendance data * 
    📈 Attendance visualization using charts --- ## 
    🧠 Technologies Used 
    Programming Language *
     Python Libraries and Frameworks
      * OpenCV (Face detection and recognition) 
      * CustomTkinter (Graphical user interface)
      * NumPy
      * Pandas 
      * Matplotlib Database
      * MySQL Tools 
      * MySQL Workbench 
      * Git * GitHub 
      * VS Code 
      --- ## 🏗 System Architecture Camera → Face Detection → Face Recognition → Student Identification → Attendance Marking → Database Storage → Dashboard Visualization 
      --- ## 🤖 Algorithms Used ### 
      1️⃣ Haar Cascade Algorithm Used for **face detection**. It detects faces from the camera frame using trained Haar features. ### 
      2️⃣ LBPH (Local Binary Pattern Histogram) Used for **face recognition**. This algorithm compares the detected face with trained images and predicts the student ID. Advantages: * Works well with small datasets * Fast real-time recognition * Simple and efficient --- ##
      
      
       📂 Project Structure
Smart-Attendance-System
│
├── student.py
├── train.py
├── face_recognition.py
├── attendance.py
├── dashboard.py
├── login.py
│
├── dataset/
│
├── classifier.xml
│
├── student_database.sql
│
├── requirements.txt
│
└── README.md
--- ## 🗄 Database Design ### Student Table
 | Column | Description | 
 | ------------ | ---------------------- |
  | student_id | Unique student ID | 
  | roll | Roll number | 
  | name | Student name | 
  | department | Department | 
  | photo_sample | Face dataset reference 
  
  | ### Attendance Table
   | Column | Description |
    | ---------- | ----------------- |
    | id | Auto increment ID |
    | student_id | Student ID |
    | roll | Roll number | 
    | name | Student name |
    | time | Attendance time | 
    | date | Attendance date | 
    | status | Present / Absent | --- ## ⚙ Installation ### 1️⃣ Clone Repository
git clone https://github.com/yourusername/smart-attendance-system.git
### 2️⃣ Install Requirements
pip install -r requirements.txt
### 3️⃣ Setup Database Import the SQL file into MySQL:
student_database.sql
### 4️⃣ Run the Program
python login.py
--- ## 🎯 How the System Works 
1. Admin registers students in the system 
2. Face dataset is generated using the camera 
3. Training algorithm creates a recognition model 
4. Camera detects and recognizes faces 
5. Attendance is automatically stored in the database 
6. Dashboard displays attendance statistics 
--- ## 📊 Dashboard The dashboard shows: 
* Total students 
* Present students 
* Absent students 
* Attendance charts This helps administrators monitor attendance in real time. 
--- ## ⚡ Advantages 
* Eliminates manual attendance 
* Prevents proxy attendance 
* Saves time 
* Contactless attendance system 
* Real-time attendance analytics
 --- ## 🔮 Future Improvements 
 * Cloud database integration 
 * Mobile application support 
 * Deep learning face recognition 
 * Multi-camera attendance system 
 * Attendance reports export (PDF/Excel) 
 
 --- ## 🎓 Applications 
 * Colleges and universities 
 * Schools 
 * Offices and organizations 
 * Security systems 
 * Smart classrooms 
