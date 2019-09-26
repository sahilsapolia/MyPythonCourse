def print_movie_info(movie,year):
    '''Prints fomatted string'''
    print(f'The movie {movie} is from {year}')

def movie_info(movie,year):
    message = "The movie " + movie + " is from " + str(year)
    return message

movie_name="Matrix"
movie_year=2002

print_movie_info(movie_name,movie_year)

print(movie_info(movie_name,movie_year))

movie_list={"Matrix1":2002,"Matrix2":2004, "Matrix3":2006}

for movie,year in movie_list.items():
    print_movie_info(movie,year)

