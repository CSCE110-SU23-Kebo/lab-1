uin = str() # Construct an empty string
valid = False
while not valid:
    offset = 0
    uin = input("Enter UIN: ")
    if uin.isnumeric() and len(uin) == 9:
        offset = abs(int(uin[0]) - int(uin[-1]))
    valid = uin.isnumeric() and len(uin) == 9 and offset >= 4

    if not valid:
        print(f"Invalid UIN\n")
else:
    print(f"Valid UIN")