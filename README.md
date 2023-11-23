# Netflix-Recommendation-Algorithm
A Netflix movie recommendation algorithm based on the genres the user likes the most.
Displays the top five movies based on the genres the user likes.

How it works:

  1. The CSV file containing information on Netflix titles such as title name, year of release, ratings, actors, and description is turned
     into a data frame using pandas, at the same time clearing any duplicates.

  2. The first function called is watched_movies(), which asks the users for the Netflix titles they have watched and stores them in a list. The method
     checks if the title is in the data frame.

  3. The second function called is watched_genres() which takes the list from watched_movies() as an argument. The function checks each title genre using the get_genres()
     function and creates a dictionary containing the genre type as the key and how many times the genre has been watched by the user as the value.

  4. The third function is the sort_genres() method which sorts the genres by most popular relative to the user.

  5. The movies_filtered() function filters out all the titles with ratings less than 7.0 and that have been watched by the user

  6. Finally, the recommend_movies() function takes the user's favourite genres and returns a list of five titles the user should watch

This program uses collaborative filtering to recommend movies.

What I learned from this project:
  1. How to use the PANDAS module
  2. Improved my efficiency by creating separate functions for certain tasks to reduce repetition
  3. Improved my skill with simple data structures such as Dictionaries.
