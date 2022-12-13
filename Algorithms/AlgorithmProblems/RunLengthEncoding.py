def run_length_encoding(input_string):
    output_string = ""
    for i in range(0, len(input_string), 2):
        output_string = output_string + int(input_string[i]) * input_string[i + 1]

    return output_string


def run_length_decoding(input_string):
    output_string = ""
    flag = 1
    current_letter = input_string[0]
    for i in range(len(input_string)):
        if current_letter == input_string[i + 1]:
            flag = flag + 1
            if i + 2 == len(input_string):
                output_string = output_string + str(flag) + current_letter
                break

        else:
            output_string = output_string + str(flag) + current_letter
            current_letter = input_string[i + 1]
            flag = 1
        if flag == 9:
            output_string = output_string + str(flag) + current_letter
            flag = 0

    return output_string


string1 = "9a4a2b1c6n"
string2 = "aaaaaaaaaaaaabbcnnnnnnnnnnn"
print(run_length_encoding(string1))
print(run_length_decoding(string2))
