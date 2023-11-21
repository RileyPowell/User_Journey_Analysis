import pandas as pd
import re
test_df = pd.read_csv('user_journey_raw.csv')
pd.set_option('display.max_columns',None)
# user_journey_col = df['user_journey']

def Repeat_Cleaner(dataframe,column_to_be_cleaned):
    """Given a string column that contains the webpages a user has visited this function
    deletes the sections of the string that are repeated and are in series.
    example: "log-in log-in homepage" --> "log-in homepage"

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_be_cleaned (string): the name of the column that contains the user_journey.

    Returns:
    dataframe: the same dataframe with the user_journey column cleaned of repeat values.

   """

    dataframe = dataframe.copy(deep=True)
    user_journey_col = dataframe[column_to_be_cleaned]
    for index,value in user_journey_col.items():
        if " " in value:
            pass
        else:
            value = value.replace('-',' ')

        web_pages = value.split()
        for i in reversed(range(len(web_pages)-1)):
            if web_pages[i] == web_pages[i+1]:
                del web_pages[i]
        web_pages = " ".join(web_pages)
        dataframe.loc[index,column_to_be_cleaned] = web_pages
    return dataframe

def grouping_strings(data,n=None):
    """This function concatenates the user_journey column strings together grouped by the user_id column
    and can be limited to the first n user entries.

    Parameters:
    data (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    number_of_cols (int): the number of entries that should be grouped together, if undefined then all entries.

    Returns:
    dataframe: containing all the original columns with the user_journey column modified.

   """

    if n == None:
        df = data.copy(deep=True)
    else:
        df = data.groupby('user_id').head(n).copy(deep=True)
    return df.groupby(['user_id'], as_index=False).agg({'user_journey':" ".join})



def Unnecessary_value(dataframe,pages_to_remove,column_to_be_cleaned):
    """removes a specified webpage from every entry in the user_journey column.

    Parameters:
    dataframe: a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    pages_to_remove (string or list of strings): the webpages that are being removed.

    Returns:
    dataframe: contains all the original columns with the modified user_journey column.

   """


    dataframe = dataframe.copy(deep=True)
    if isinstance(pages_to_remove,list):
        for i in pages_to_remove:
            temp_df = Unnecessary_value(dataframe,i,column_to_be_cleaned)
            dataframe = temp_df.copy(deep=True)
    dataframe = dataframe.copy(deep=True)
    user_journey_col = dataframe[column_to_be_cleaned]
    for index,value in user_journey_col.items():
        web_pages = value.split()
        try:
            web_pages.remove(pages_to_remove)
        except:
            continue
        web_pages = " ".join(web_pages)
        dataframe.loc[index,column_to_be_cleaned] = web_pages
    return dataframe

cleaned_df = Repeat_Cleaner(test_df,'user_journey')
cleaned_grouped_df = grouping_strings(cleaned_df)
preprocessed_data = Unnecessary_value(cleaned_grouped_df,'in-Log','user_journey')
preprocessed_data.to_csv('Preprocessed_data.csv',index=False)