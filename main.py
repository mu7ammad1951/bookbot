def count_words(text):
    number_of_words = len(text.split())
    return number_of_words

def sort_on(dict):
    return dict["count"]

def count_characters(text):
    count_of_characters = {}
    for string in text:
        string = string.lower()
        for character in string:
            if character.isalpha():
                if character in count_of_characters:
                    count_of_characters[character] += 1
                else:
                    count_of_characters[character] = 1
    return convert_to_list(count_of_characters)

def convert_to_list(count_of_characters):
    list_of_counts = []
    for character in count_of_characters:
        list_of_counts.append({"character":character, "count":count_of_characters[character]})
    return list_of_counts

def print_report(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(text)} words found in the document.\n")
    count_of_characters = count_characters(text)
    count_of_characters.sort(reverse=True, key=sort_on)
    for count in count_of_characters:
        print(f"The character {count["character"]} occured {count["count"]} times in the document.")
    print("--- END OF REPORT ---")

def __main__():
    path_to_file = "./books/frankenstein.txt"
    print_report(path_to_file)

__main__()