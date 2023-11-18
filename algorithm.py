import pandas as pd

movie_df = pd.read_csv("movies_with_ratings.csv").drop_duplicates(subset="title").dropna().reset_index(drop=True)

# Checks if the argument title is in the data set of titles
def is_valid_movie_name(movie_title):
    for title in movie_df["title"].str.lower():
        if movie_title == title:
            return True
    return False

# Locates the index of the title in the data set
def locate_movie_row(movie_title):
    index = movie_df.index[movie_df['title'].str.lower() == movie_title]
    return index[0]

# Returns the genres of a certain title in a list
def get_genres(movie_title):
    genre_list = []
    temp = movie_df.iloc[locate_movie_row(movie_title), 4].split(", ")
    for genre in temp:
        genre_list.append(genre)
    return genre_list

# Asks the user for titles they have watched. Returns a list of the titles. Titles are checked if they are in the data set
def watched_movies():
    watched_titles = []
    while True:
        user_input = input("Enter a title you've watched or enter \"0x0\" to exit: ").lower()
        if user_input == "0x0":
            break
        else:
            if is_valid_movie_name(user_input) and user_input in watched_titles:
                print("You have already seen this title. Please enter a different title.\n")
            elif is_valid_movie_name(user_input):   
                watched_titles.append(user_input)
                print("Title added to watched list\n")
            else:
                print("Invlaid title name\n")
    return watched_titles

# Returns a dictioanry of genres and how many times they have been watched by the user
def watched_genres(titles_watched):
    genres = {}
    for movie in titles_watched:
        genre_list = get_genres(movie)
        for genre in genre_list:
            if genre not in genres:
                genres[genre] = 1
            else:
                genres[genre] += 1
    return genres    

# Sorts the favourite genres by how many times they've been watched and returns the five most popular genre for the user, if less than five genres are given
# Then the top n<5 genres are returned
def sort_genres(genre_dict):
    favourite_genres = []
    sorted_list = sorted(genre_dict.items(), key=lambda x:x[1], reverse=1)
    if len(sorted_list) >= 5:
        for i in range(0,5):
            favourite_genres.append(sorted_list[i][0])
    else:
        for genre in sorted_list:
            favourite_genres.append(genre[0])
    return favourite_genres

# Returns a data set of the titles that have not been watched by the user and are rated over 7.0
def movies_filtred(watched_movies_list):
    movie_df_7up_ratings = movie_df[movie_df["rating"] >= 7.0].reset_index(drop=True)
    movie_df_7up_ratings = movie_df_7up_ratings[~movie_df_7up_ratings["title"].str.lower().isin(watched_movies_list)]
    return movie_df_7up_ratings.reset_index(drop=True)

def recommend_movies(fav_genres, sorted_movies):
    good_movies = pd.DataFrame()
    for genre in fav_genres:
        genre_movies = sorted_movies[sorted_movies["genre"].str.contains(genre)]
        good_movies = pd.concat([good_movies, genre_movies])
    top_5_titles = []
    for i in range(0,5):
        top_5_titles.append(good_movies.iloc[i,0])
    return top_5_titles

def display_recommended_titles(top_5_list):
    print("Top 5 Movies to Watch")
    print("----------------------------")
    for title in top_5_list:
        print(title)
    print("----------------------------")
        

