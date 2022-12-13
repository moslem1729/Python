

wanted_string=input("enter first input:")
given_string=input("enter second input:")

output=0
for i in range(len(given_string)-len(wanted_string)):
    if given_string[i:i+len(wanted_string)]==wanted_string:
        output=1

print(output)