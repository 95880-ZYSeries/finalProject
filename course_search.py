import pandas as pd


def search_course_by_code(course_code, course_df):
    """
    Arguments:
        course_code {string} -- a string represents course number, e.g. '15213'
        course_df: {DataFrame} -- a dataframe of all information.

    Returns:
        DataFrame - a DataFrame contains the relevant information of the relevant course_code
    """
    course_code = int(course_code)
    return course_df[course_df.course_number==course_code]


def search_course_by_school_code(school_code, level, course_df):
    """
    Arguments:
        school_code {String} -- a string represents the school number, e.g. '95' for IS department
        level {String} -- a string 'U'/'V' represents the course level.
        course_df: {DataFrame} -- a dataframe of all information.

    Returns:
        DataFrame - a DataFrame contains the relevant information of the relevant course_code

    """
    school_code = int(school_code)
    ans = []
    for index,item in course_df.iterrows():
        if int(item.course_number/1000)==int(school_code):
            if level=='U':
                if int(item.course_number/100)%10<6:
                    ans.append(item)
            else:
                if int(item.course_number/100)%10>=6:
                    ans.append(item)
    
    ans_df = pd.DataFrame(data=ans)
    if len(ans_df)>0:
        ans_df.sort_values(by=['course_rate'], ascending=False, inplace=True)
    return ans_df


def search_course_by_course_name(course_name, course_df):
    """
    Arguments:
        course_name: {String} --  a keyword represents the topic user want to search
        course_df: {DataFrame} -- a dataframe of all information.

    Returns:
        DataFrame - a DataFrame contains the relevant information of the relevant course_code

    """
    course_name = course_name.lower()
    ans = []
    for index, item in course_df.iterrows():
        if item.course_name.lower().find(course_name)>=0:
            print(item.course_name)
            ans.append(item)
    ans_df = pd.DataFrame(data=ans)
    if len(ans_df)>0:
        ans_df.sort_values(by=['course_rate'], ascending=False, inplace=True)
    return ans_df

