def acro(name):
    if not name:
        raise ValueError("Empty string has no acronym")
        
    acronym = ""
    for word in name.strip().split():
        acronym += word[0].upper()

    return acronym

    # One list solution with filter
    return "".join(filter(str.isupper, name.strip().title()))

if __name__ == '__main__':
    name = input("What is the name? ")
    print(f"Its acronym is {acro(name)}.")