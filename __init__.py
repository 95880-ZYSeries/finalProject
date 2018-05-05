from tabulate import tabulate
import pandas as pd
from search_instructor import search_instr
from course_search import search_course_by_code, search_course_by_school_code, search_course_by_course_name


def main():
    """
    Build DataFrame from CSV file and read input and call corresponding functions

    """
    course_df = pd.read_csv('course.csv', index_col=None, header=0);
    instructor_df = pd.read_csv('instructor.csv', index_col=None, header=0);

    while True:
        print()
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

        # distribute actions to different functions
        num = input()
        while not num.isdigit():
            num = input("Please enter a correct number: ")
        if num == '1':
            course_code(course_df)
        elif num == '2':
            school_code(course_df)
        elif num == '3':
            course_name(course_df)
        elif num == '4':
            instructor(instructor_df)
        elif num == '5':
            get_help()
        elif num == '6':
            print("Thanks!")
            break
        else:
            print()
            print("Sorry! We don't have the function number you entered.")


# let the user enter the course number they want to search and return the relevant course
def course_code(course_df):
    """
        Arguments:
            course_df: {DataFrame} - a DataFrame contains all course info
    """
    try:
        code = input("Please enter a five-digit course code: ")
        if not code.isdigit():
            print('Invalid course code')
            course_code(course_df)
        else:
            df = search_course_by_code(code, course_df)
            if len(df) == 0:
                print()
                print("Sorry! We cannot find this course.")
                return
            print(tabulate(df, headers='keys', tablefmt='psql'))
    except Exception:
        course_code(course_df)


# let the user enter the school code and course_level they want to search and return the relevant course
def school_code(course_df):
    """
        Arguments:
            course_df: {DataFrame} - a DataFrame contains all course info
    """
    try:
        code = input("Please enter a two-digit school code: ")
        level = input("Please enter your level(U for undergraduate, G for graduate):")
        if (len(code) != 2) or (not code.isdigit()):
            print('Invalid school code')
            school_code(course_df)
            return
        if level != 'U' and level != 'G':
            print('Invalid level')
            school_code(course_df)
            return
        else:
            df = search_course_by_school_code(code, level, course_df)
            if df is None or len(df) == 0:
                print()
                print("Sorry! We cannot find course in this condition.")
                return
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except Exception:
        school_code(course_df)


# let the user enter the topic they want to search and return the relevant course
def course_name(course_df):
    """
        Arguments:
            course_df: {DataFrame} - a DataFrame contains all course info
    """
    try:
        name = input("Please enter a keyword of course name: ")
        df = search_course_by_course_name(name, course_df)
        if df is None or len(df) == 0:
            print()
            print("Sorry! We cannot find the course with this keyword.")
            return
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except Exception:
        course_name(course_df)


# let the user enter the topic they want to search and return the relevant course
def instructor(instructor_df):
    """
        Arguments:
                instructor_df: {DataFrame} - a DataFrame contains all instructor info
    """
    try:
        name = input("Please enter the name of an instructor: ")
        df = search_instr(instructor_df, name)
        if len(df) == 0:
            print()
            print("Sorry! We cannot find the instructor.")
            return
        print(tabulate(df, headers='keys', tablefmt='psql'))

    except Exception:
        search_instr(instructor_df)


# show helper.txt
def get_help():
    print("**********************************************************************************************************")
    print()
    print('                                                   Help                                                   ')
    print()
    print("**********************************************************************************************************")
    help_file = open('helper.txt', 'r')
    text = help_file.read()
    print(text)


if __name__ == "__main__":
    main()



