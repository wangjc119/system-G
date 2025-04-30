import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from Student import Student
from Teacher import Teacher
from Course import Course

def main():
    choice = input('請選擇角色: 1 教師 2 學生: ')
    
    if choice == '1':
        teachers = [Teacher('王老師'), Teacher('朱老師')]

        for teacher in teachers:
            while True:
                try:
                    email = input(f"請輸入 {teacher.getName()} 的 email: ")
                    teacher.setEmail(email)
                    break
                except ValueError as e:
                    print(e)

        print("\n教師名單與Email：")
        for index, teacher in enumerate(teachers, 1):
            print(f"{index}. {teacher.getName()} - {teacher.getEmail()}")

    elif choice == '2':
        students = [Student('張學生'), Student('范學生')]

        for student in students:
            while True:
                try:
                    email = input(f"請輸入 {student.getName()} 的 email: ")
                    student.setEmail(email)
                    break
                except ValueError as e:
                    print(e)

        print("\n學生名單與Email：")
        for index, student in enumerate(students, 1):
            print(f"{index}. {student.getName()} - {student.getEmail()}")

        choice2 = input(f"\n歡迎進入選課系統: 請選擇學生 1 張學生 2 范學生: ")    
        
        courses = [
            Course('國文 必修 星期一 13:10~15:00'),
            Course('英文 必修 星期二 08:10~10:00'),
            Course('數學 必修 星期三 09:10~12:00'),
            Course('自然 選修 星期四 15:10~16:00'),
            Course('社會 選修 星期五 10:10~12:00')
        ]

        print("\n可選課程：")
        for index, course in enumerate(courses, 1):
            print(f"{index}. {course.getName()}")

        selected_courses = []
        while True:
            course_choice = input("\n請輸入你想選擇的課程編號 (或輸入0結束): ")
            if course_choice == '0':
                break
            elif course_choice in ['1', '2', '3', '4', '5']:
                selected_courses.append(courses[int(course_choice)-1])
                print(f"你已選擇: {courses[int(course_choice)-1].getName()}")
            else:
                print("無效的課程編號，請重新輸入。")

        print("\n你選擇的課程是：")
        for course in selected_courses:
            print(course.getName())

    else:
        print('輸入錯誤')

if __name__ == "__main__":
    main()
