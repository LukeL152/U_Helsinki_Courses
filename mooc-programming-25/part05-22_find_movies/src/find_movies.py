# Write your solution here
def find_movies(database: list, search_term: str):
    results = []
    search_term = search_term.lower()
    for i in database:
        if search_term in i["name"].lower():
            results.append(i)
    return results
