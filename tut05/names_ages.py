from datetime import datetime

people = []


def add_name_age(name, dob):
    people.append({"name": name, "age": date_to_age(dob)})


# min_age acts as an optional argument, with a default value of None
def get_names_ages(min_age=None):
    if min_age is None:
        return people
    return list(filter(lambda person: person["age"] >= int(min_age), people))


def clear_names_ages():
    people.clear()


def edit_name_age(name, dob):
    for name_age in people:
        if name_age["name"] == name:
            name_age["age"] = date_to_age(dob)
            return


def date_to_age(dob):
    """
    Helper function that takes in a date of birth string and returns their age
    """
    today = datetime.today()
    dob_obj = datetime.strptime(dob, "%d-%m-%Y")
    years = today.year - dob_obj.year
    if today.month < dob_obj.month or (
        today.month == dob_obj.month and today.day < dob_obj.day
    ):
        years -= 1
    return years
