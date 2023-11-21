import pandas as pd
from statistics import mode
from collections import Counter
def  possible_pages(dataframe,column_to_check):
    """Iterate over every webpage viewed by every user and make a list of all unique values.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.

    Returns:
    list: all unique webpage entries.

   """

    unique_pages = []
    for idx,value in dataframe[column_to_check].items():
        page_ls = value.split()
        unique_pages.extend(page_ls)
        unique_pages = set(unique_pages)
        unique_pages = list(unique_pages)
    return unique_pages




def journey_length(dataframe,column_to_check):
    """How many webpages users have visited appended to a new column in the dataframe.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.

    Returns:
    dataframe: the original dataframe with a new column containing the integer number of webpages visited by a user.

   """

    lengths = []
    for idx,val in dataframe[column_to_check].items():
        pages = val.split()
        lengths.append(len(pages))
    dataframe['journey_length'] = lengths
    return dataframe

def most_common_run(dataframe,column_to_check,n):
    """This function finds the most common run of webpages of length n.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.
    n (int): how many webpages should be considered a run.

    Returns:
    dataframe: the original dataframe with a new column added that contains the most common webpage run.

   """

    coms = []
    for idx,val in dataframe[column_to_check].items():
        temp = []
        pages = val.split()
        for i in range(len(pages)):
            temp.append(",".join(pages[i:i+n]))
        # print((temp))
        # break
        coms.append(mode(temp).split(','))

    dataframe['most_common_run'] = coms
    return dataframe


def page_destination(dataframe,column_to_check):
    """The most common webpage visited after each webpage.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.

    Returns:
    dict: a dictionary where the keys are the unique webpages and the values are a two element list containing the
    most common following web and the number of times it was the following the webpage.

   """

    pages = possible_pages(df,'user_journey')
    temp = []
    for idx,val in dataframe[column_to_check].items():
        val = val.split()
        for i in range(len(val)):
            temp.append(val[i:i+2])
    dick = {}
    for page in pages:
        temp_2 = []
        for twin in temp:
            if twin[0] == page and len(twin)>1:
                temp_2.append(''.join(twin[1]))
        # now find the most common using mode of counter .most_common then split them again and add the page
        # to a dict as the key and the count as the value
        if len(Counter(temp_2).most_common(1)) == 0:
            dick[page] = ["",0]
        else:
            dick[page] = list(Counter(temp_2).most_common(1)[0])
    return dick
def page_presence(dataframe,column_to_check,user_id,pages):
    """This function finds which webpages are present in a users journey.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.
    user_id (int): the ID of the user whose journey is being analyzed.
    pages (list): the list containing all the unique webpages.

    Returns:
    dict: a dictionary where the keys are the webpage and the values are either a 1 or 0 representing page presence or
    absence respectively.

   """

    dataframe.set_index(dataframe['user_id'],inplace=True)
    webpages = dataframe[column_to_check][user_id].split()
    diction = {}
    for page in pages:
        if page in webpages:
            diction[page] = 1
        else:
            diction[page] = 0
    return diction

def page_count(dataframe,column_to_check,user_id,pages):
    """Count the number of times each webpage occurs in a users webpage journey.

    Parameters:
    dataframe (dataframe): a dataframe of user_ids, session_ids, subscription types, and the user_journey.
    column_to_check (string): the name of the column containing the user_journey data.
    user_id (int): the ID of the user whose journey is being analyzed.
    pages (list): the list containing all the unique webpages.

    Returns:
    a dictionary where the keys are the webpage and the values are the number of times the page is in the users journey

   """

    dataframe.set_index(dataframe['user_id'],inplace=True)
    webpages = dataframe[column_to_check][user_id].split()
    diction = {}
    for page in pages:
        if page in webpages:
            diction[page] = webpages.count(page)
        else:
            diction[page] = 0
    return diction

df = pd.read_csv('Preprocessed_data.csv')
pages = possible_pages(df,'user_journey')
most_com = most_common_run(df,'user_journey',3)
destinations = page_destination(df,"user_journey")
presence = page_presence(df,'user_journey',1516,pages)
cnt = page_count(df,'user_journey',1516,pages)

