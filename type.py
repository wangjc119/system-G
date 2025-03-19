import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# 引入必要的類別
from Student import Student
from Teacher import Teacher
from Course import Course

def main():
    choice = input('請選擇角色: 1 教師 2 學生: ')
    
    if choice == '1':
        # 教師角色，建立教師實例
        teacher1 = Teacher('王老師')
        teacher2 = Teacher('朱老師')
        teacher1.getName()
        teacher2.getName()
    
    elif choice == '2':
        # 學生角色，建立學生實例
        
        students = []
        while True:
            student_name = input("請輸入學生的名字 (輸入0結束): ")
            if student_name == '0':
                break
            else:
                new_student = Student(student_name)
                students.append(new_student)
                print(f"已添加學生: {student_name}")

        # 顯示所有學生並讓使用者選擇
        print("\n學生列表：")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.name}")

        choice2 = input(f"\n請選擇學生: (輸入學生編號): ")
        if choice2.isdigit() and 1 <= int(choice2) <= len(students):
            selected_student = students[int(choice2) - 1]
            print(f"你選擇的學生是: {selected_student.name}")
        else:
            print("無效的學生編號")

        # 顯示可選課程
        courses = []
        while True:
            course_name = input("請輸入課程名稱 (輸入0結束): ")
            if course_name == '0':
                break
            else:
                new_course = Course(course_name)
                courses.append(new_course)
                print(f"已添加課程: {course_name}")

        print("\n可選課程：")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course.name}")

        # 讓學生選擇課程
        selected_courses = []
        while True:
            course_choice = input("\n請輸入你想選擇的課程編號 (或輸入0結束): ")
            if course_choice == '0':
                break
            elif course_choice.isdigit() and 1 <= int(course_choice) <= len(courses):
                selected_courses.append(courses[int(course_choice)-1])
                print(f"你已選擇: {courses[int(course_choice)-1].name}")
            else:
                print("無效的課程編號，請重新輸入。")

        # 顯示選擇的課程
        print("\n你選擇的課程是：")
        for course in selected_courses:
            course.getName()

    else:
        print('輸入錯誤')

if __name__ == "__main__":
    main()
