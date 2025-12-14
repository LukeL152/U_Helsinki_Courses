# Write your solution here
def older_people(people: list, year: int):
    older_people = []
    for person in people:
        if person[1] < year:
            older_people.append(person[0])
    return older_people

