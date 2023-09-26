import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("face-10f0a-firebase-adminsdk-jocqe-1cef07edc2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-10f0a-default-rtdb.asia-southeast1.firebasedatabase.app"
})

ref = db.reference('Students')

data = {
    "123321":
        {
            "name": "Nguyễn Anh Tùng",
            "major": "Lập Trình Viên",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "235432":
        {
            "name": "Đỗ Ngọc Hữu",
            "major": "Trưởng phòng",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Nguyễn Thị Khoa",
            "major": "cơ phó",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)