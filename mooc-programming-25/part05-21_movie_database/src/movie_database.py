# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_dict = {}
    movie_dict["name"] = name
    movie_dict["director"] = director
    movie_dict["year"] = year
    movie_dict["runtime"] = runtime
    database.append(movie_dict)
