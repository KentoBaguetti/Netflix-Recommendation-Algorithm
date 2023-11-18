from algorithm import *

def main():
    list_movies_watched = watched_movies()
    user_watched_genres = watched_genres(list_movies_watched)
    filtered_movies = movies_filtred(list_movies_watched)
    top_5_movies_for_rec = recommend_movies(user_watched_genres, filtered_movies)
    display_recommended_titles(top_5_movies_for_rec)
    
main()