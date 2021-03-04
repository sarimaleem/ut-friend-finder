from src.models import User
import functools

import sys

def ranking(user: User) -> int:
    ranker = functools.partial(rank, user)
    return sorted([User.query.all()], key=ranker)

def rank(a: User, b: User):
    """
    Compares to students to each other, and returns their compat_index
    """
    compat_index = 0

    location_weight = 5
    school_weight = 5
    major_weight = 8
    classif_weight = 2
    age_weight = 2


    if a.location == b.location:
        compat_index += location_weight

    if a.school == b.school:
        compat_index += school_weight

    if a.major == b.major:
        compat_index += major_weight

    if a.classification == b.classification:
        compat_index += classif_weight

    if a.age == b.age:
        compat_index += age_weight

    return compat_index

def main():
    #                0   1     2      3       4      5         6         7
    #format will be "ID NAME EMAIL LOCATION SCHOOL MAJOR CLASSIFICATION AGE"
    #will gender matter? how will we handle the classes theyre in?

    # weights are arbitrarily chosen and range from 1-10

    # user is first line of input
    this_user = sys.stdin.readline().strip().split()
    this_location = this_user[3]
    this_school = this_user[4]
    this_major = this_user[5]

    if (this_user[6] == "FRESHMAN"):
        this_classif = 0
    elif (this_user[6] == "SOPHOMORE"):
        this_classif = 1
    elif (this_user[6] == "JUNIOR"):
        this_classif = 2
    else:
        this_classif = 3

    this_age = int(this_user[7])

    # each of the following lines are the other users of the app
    other_user = sys.stdin.readline().strip().split()
    rec_matches = []

    while (other_user):
        compat_index = 0

        other_id = other_user[0]
        other_location = other_user[3]
        other_school = other_user[4]
        other_major = other_user[5]

        if (other_user[6] == "FRESHMAN"):
            other_classif = 0
        elif (other_user[6] == "SOPHOMORE"):
            other_classif = 1
        elif (other_user[6] == "JUNIOR"):
            other_classif = 2
        else:
            other_classif = 3

        other_age = int(other_user[7])

        # Would this just be a dorm or apartment name? I mean, is there code out there that could tell us the distance between 2 specific adresses?
        if(this_location == other_location):
            compat_index += 1*location_weight
        if (this_school == other_school):
            compat_index += 1*school_weight
        if (this_major == other_major):
            compat_index += 1*major_weight
        compat_index += (3 - abs(this_classif - other_classif)) * classif_weight
        compat_index += (3 - abs(this_age - other_age)) * age_weight

        rec_matches.append((compat_index, other_id))
        other_user = sys.stdin.readline().strip().split()

    print(sorted(rec_matches, reverse=bool(1)))

if __name__ == "__main__":
    main()
