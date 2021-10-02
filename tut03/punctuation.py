import string

# Method 1 - Using with, join and .write
def method_1():
    with open('tolstoy.txt') as tolstoy:
        with open('no_punctuation.txt', 'w') as out_file:
            for line in tolstoy:
                words = line.split()
                stripped_words = []
                for word in words:
                    stripped_words.append(word.strip(string.punctuation))
                out_file.write(" ".join(stripped_words) + "\n")


# Method 2 - Using print
def method_2():
    with open('tolstoy.txt') as tolstoy, open('no_punctuation.txt', 'w') as out:
        for line in tolstoy:
            words = line.split()
            for word in words:
                print(word.strip(string.punctuation), end=' ',file=out)
            print(file=out)

# Method 3 - Not using with/as
def method_3():
    tolstoy = open('tolstoy.txt')
    output = open('no_punctuation.txt', 'w')
    for line in tolstoy:
        words = line.split()
        for word in words:
            output.write(f"{word.strip(string.punctuation)} ")
        output.write("\n")
    tolstoy.close()
    output.close()

if __name__ == "__main__":
    # method_1()
    # method_2()
    method_3()
