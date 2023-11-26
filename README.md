# User_Journey_Analysis
Hello and welcome to an anlysis of users journeys through a set of webpages. This project uses a public data set to create a pipeline that cleans, transforms, and creates several metrics based on a users journey through webpages. The data is given as a CSV with the following columns: user_id (int(4)), session_id (int(7)), subscription_type (string), user_journey (string).
The project is split into two Python files Preprocessing.py and Analysis.py:
* Preprocessing.py contains three functions: Repeat_cleaner, grouping_strings, unnecessary_value.
  * Repeat_cleaner: Iterates through the user_journey column and removes webpages that are repeated sequentially.
  * grouping_strings: Concatenates the user_journey column together based on grouping the user_id's.
  * unnecessary_value: Removes every instance of a specific webpage from every user_journey.
* Analysis.py contains five functions: possible_pages, journey_length, most_common_run, page_destination, page_presence, page_count.
  * possible_pages: Get a list of every unique webpage from all the user_journeys
  * journey_length: Add a column to the dataset that contains how many webpages the user visits throughout their journey.
  * most_common_run: Add a column containing the most common run of n number of webpages in each users journey.
  * page_destination: Return a dictionary containing every webpage as a key and the most common webpage after it in user_journey as the value.
  * page_presence: Return a dictionary containing every webpage as a key and either a 1 or a 0 to indicate if the webpage appeared in the specified users journey.
  * page_count: Return a dictionary containing every webpage as a key and a count of how many times the webpage appeared in the specified users journey.
