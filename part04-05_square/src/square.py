def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def square(size, character):
    i = 1
    while i <= size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")