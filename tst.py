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
        # 教師角色，創建教師實例
        teachers = [Teacher('王老師'), Teacher('朱老師')]
        
        print("教師名單：")
        for index, teacher in enumerate(teachers, 1):
            print(f"{index}. {teacher.getName()}")  # getName 返回名稱
    
    elif choice == '2':
        # 學生角色，創建學生實例
        students = [Student('張學生'), Student('范學生')]
        
        print("學生名單：")
        for index, student in enumerate(students, 1):
            print(f"{index}. {student.getName()}")  # getName 返回名稱

        # 學生選擇後，顯示課程
        choice2 = input(f"\n歡迎進入選課系統: 請選擇學生 1 張學生 2 范學生: ")    
        
        courses = [
            Course('國文 必修 星期一 13:10~15:00'),
            Course('英文 必修 星期二 08:10~10:00'),
            Course('數學 必修 星期三 09:10~12:00'),
            Course('自然 選修 星期四 15:10~16:00'),
            Course('社會 選修 星期五 10:10~12:00')
        ]

        # 顯示可選課程
        print("可選課程：")
        for index, course in enumerate(courses, 1):
            print(f"{index}. {course.getName()}")  # getName 返回名稱

        # 讓學生選擇課程
        selected_courses = []
        while True:
            course_choice = input("\n請輸入你想選擇的課程編號 (或輸入0結束): ")
            if course_choice == '0':
                break
            elif course_choice in ['1', '2', '3', '4', '5']:
                selected_courses.append(courses[int(course_choice)-1])
                print(f"你已選擇: {courses[int(course_choice)-1].name}")
            else:
                print("無效的課程編號，請重新輸入。")

        # 顯示選擇的課程
        print("\n你選擇的課程是：")
        for course in selected_courses:
            print(course.getName())  # getName 返回名稱

    else:
        print('輸入錯誤')

if __name__ == "__main__":
    main()
