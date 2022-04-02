NAME_PLACEHOLDER = "[name]"

with open(".\\Input\\Names\\invited_names.txt") as names_file:
    names = names_file.readlines()


with open(".\\Input\\Letters\\starting_letter.docx") as letter_file:
    letter = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter.replace(NAME_PLACEHOLDER, name)
        print(new_letter)
        with open(".\\Output\\ReadyToSend\\example.docx") as completed_letter:
            print(completed_letter)