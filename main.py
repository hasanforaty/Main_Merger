with open("./Input/Letters/starting_letter.txt") as start_letter:
    template = start_letter.readlines()
    with open('./Input/Names/invited_names.txt') as name_file:
        names = name_file.readlines()
        for name in names:
            with open('./Output/ReadyToSend/letter_to_'+name.strip()+'.txt', 'w') as output:
                for letter in template:
                    output.write(letter.replace('[name]', name.strip()))



