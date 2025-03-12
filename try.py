import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# Importing the necessary classes from other modules
from Student import Student
from Teacher import Teacher
from Course import Course

def main():
    choice = input('请选择角色: 1 教师 2 学生: ')
    
    if choice == '1':
        # For the teacher role, create teacher instances
        teacher1 = Teacher('王老師')
        teacher2 = Teacher('朱老師')
        teacher1.getName()
        teacher2.getName()
    elif choice == '2':
        # For the student role, create student instances
        
        student1 = Student('張學生')
        student2 = Student('范學生')
        student1.getName()
        student2.getName()

        # After student selection, show courses
        choice2 = input(f"\n欢迎进入选课系统: 請選擇學生 1張學生 2范學生")    
        course1 = Course('1.國文')
        course2 = Course('2.英文')
        course3 = Course('3.數學')
        course4 = Course('4.自然')
        course5 = Course('5.社會')

        # Display available courses
        courses = [course1, course2, course3, course4, course5]
        print("可选课程：")
        for i, course in enumerate(courses, 1):
            course.getName()

        # Option for the user to add a custom course
        add_custom_courses = input("是否想要自定义课程? (y/n): ")
        if add_custom_courses.lower() == 'y':
            while True:
                custom_course_name = input("请输入自定义课程名称 (输入0结束): ")
                if custom_course_name == '0':
                    break
                else:
                    new_course = Course(custom_course_name)
                    courses.append(new_course)
                    print(f"已添加课程: {custom_course_name}")

        # Let the student choose courses
        selected_courses = []
        while True:
            course_choice = input("\n请输入你想选择的课程编号 (或输入0结束): ")
            if course_choice == '0':
                break
            elif course_choice.isdigit() and 1 <= int(course_choice) <= len(courses):
                selected_courses.append(courses[int(course_choice)-1])
                print(f"你已选择: {courses[int(course_choice)-1].name}")
            else:
                print("无效的课程编号，请重新输入。")

        # Display selected courses
        print("\n你选择的课程是：")
        for course in selected_courses:
            course.getName()

    else:
        print('输入错误')

if __name__ == "__main__":
    main()
