
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file_2:
    names = file_2.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents = file.read()
    for x in names:
        stripped_name = x.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_to_{stripped_name}.txt", mode="w") as file_3:
            file_3.write(new_letter)
            print(f"Created letter for {stripped_name}")