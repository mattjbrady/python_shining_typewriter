import random


def random_letter_string(string):
    """Select a random index within a given string."""
    length_of_string = len(string)
    random_index = random.randint(0, length_of_string)
    return random_index


def generate_random_ascii():
    """Generate a randomly selected character from the ASCII set."""
    value = random.randint(0, 127)
    random_character = str(chr(value))
    return random_character


def random_ascii_replace(string, current_range):
    """Selects a random character in a string and replaces it
    with another random character."""
    new_string = string
    modifier = current_range
    for i in range(random.randint(0 + modifier, 5 + modifier)):
        target_index = random_letter_string(string)
        new_character = generate_random_ascii()
        new_string = new_string[:target_index] + new_character \
                                + new_string[target_index + 1:]
    return new_string

def main():
    """Runs the random_ascii_replace on a line from the film The Shining."""
    phrase = "All work and no play makes Jack a dull boy."

    for i in range(10):
        print(random_ascii_replace(phrase, i))

if __name__ == "__main__":
    main()
