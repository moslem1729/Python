def first_non_repeating_character(input_string):
    character_counts={}
    for character in input_string:
        if character not in character_counts:
            character_counts[character]=1
        else:
            character_counts[character]+=1
    for i in range(len(input_string)):
        if character_counts[input_string[i]]==1:
            return i
    return -1

string1="dsffgdsgqq"
print(first_non_repeating_character(string1))