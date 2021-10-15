from datetime import datetime

data = []

def add_name_age(name, dob):
    data.append({"name": name, "age": date_to_age(dob)})

def get_names_ages():
    return data

def clear_names_ages():
    data.clear()

# Helper
def date_to_age(dob):
    # 05-12-2000
    today = datetime.today()
    dob_obj = datetime.strptime(dob, "%d-%m-%Y")
    years = today.year - dob_obj.year
    if (today.month < dob_obj.month or (today.month == dob_obj.month and
        today.day < dob_obj.day)):
        years -= 1
    return years

if __name__ == "__main__":
    print("GOOSE")
