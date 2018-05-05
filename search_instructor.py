import pandas as pd


def search_instr(instructor_df, name):
    """
    Arguments:
        instructor_df: {DataFrame} -- a DataFrame of all instructor's info.
        name: {String} -- a keyword of instructor's name

    Returns:
        DataFrame - a DataFrame contains the relevant information of the relevant instructor name
    """
    try:
        instructor_df = pd.DataFrame(instructor_df)
        target = instructor_df[instructor_df['teacher_name'].str.contains(name, case=False)]
        target = target.sort_values(by='score', ascending=False)
        return target
    except Exception:
        search_instr(instructor_df)