import pandas as pd
from tabulate import tabulate


def search_instr(instructor_df, name):
    try:
        instructor_df = pd.DataFrame(instructor_df)

        target = instructor_df[instructor_df['teacher_name'].str.contains(name, case=False)]
        target = target.sort_values(by='score', ascending=False)

        return target

        # print(tabulate([['95880', 'Python for Developer', 'Kolowitz, Brian'],
        #                 ['95888', 'Data Focused Python', 'Kolowitz, Brian'],
        #                 ['33331', 'Physical Mechanics I', 'Quinn, Brian']], headers=['Code', 'Name', 'Instructor'], tablefmt='orgtbl'))
    except Exception:
        search_instr(instructor_df)