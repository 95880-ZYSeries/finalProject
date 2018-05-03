from tabulate import tabulate
import pandas as pd


def main():

    course_df = pd.read_csv('course.csv', index_col=False, header=0);
    instructor_df = pd.read_csv('instructor.csv', index_col=False, header=0);

    while True:
        print("**************************************************************")
        print()
        print()
        print('                   Welcome to Course Box!                     ')
        print()
        print()
        print("**************************************************************")
        print()
        print("Please select the function number you need:")
        print()
        print("1. Look up courses by course code.")
        print("2. Browse courses by school.")
        print("3. Search courses by keyword")
        print("4. Search for instructors")
        print("5. Help.")
        print("6. Quit.")
        print("**************************************************************")

        num = input()
        while not num.isdigit():
            num = input("Please enter a correct number: ")
        if num == '1':
            course_code()
        elif num == '2':
            school_code()
        elif num == '3':
            keyword()
        elif num == '4':
            instructor()
        elif num == '5':
            get_help()
        elif num == '6':
            print("Thanks!")
            break
        else:
            print("Not Found.")


def course_code():
    try:
        code = input("Please enter a five-digit course code: ")
        if len(code) != 5:
            print('Invalid course code')
            course_code()
        else:
            print(tabulate([['95880', 'Python for Developer', 'Kolowitz, Brian']], headers=['Code', 'Name', 'Instructor'], tablefmt='orgtbl'))
    except Exception:
        course_code()


def school_code():
    try:
        code = input("Please enter a two-digit school code: ")
        if len(code) != 2:
            print('Invalid school code')
            school_code()
        else:
            print(tabulate([['95880', 'Python for Developer', 'Kolowitz, Brian'],
                            ['95881', 'Web Application Development', 'Bigrigg, Michael'],
                            ['95883', 'Ethical Penetration Testing', 'Cook, Michael']], headers=['Code', 'Name', 'Instructor'], tablefmt='orgtbl'))
    except Exception:
        school_code()


def instructor():
    try:
        code = input("Please enter the name of an instructor: ")

        print(tabulate([['95880', 'Python for Developer', 'Kolowitz, Brian'],
                        ['95888', 'Data Focused Python', 'Kolowitz, Brian'],
                        ['33331', 'Physical Mechanics I', 'Quinn, Brian']], headers=['Code', 'Name', 'Instructor'], tablefmt='orgtbl'))
    except Exception:
        instructor()


def course_score():
    try:
        score = input("Please enter the target course score: ")
        float(score)
        print(tabulate([['95880', 'Python for Developer', 'Kolowitz, Brian', 4.2],
                        ['95888', 'Data Focused Python', 'Kolowitz, Brian', 4.0],
                        ['33331', 'Physical Mechanics I', 'Quinn, Brian', 3.6]], headers=['Code', 'Name', 'Instructor', 'Score'], tablefmt='orgtbl'))
    except ValueError:
        print("Score not valid.")
        course_score()


if __name__ == "__main__":
    main()



