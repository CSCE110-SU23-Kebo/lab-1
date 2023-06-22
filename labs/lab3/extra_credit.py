title1 = input("Enter phrase 1: ")
title2 = input("Enter phrase 2: ")
largest_slice = str()
matches = 0

for length in range(4,9):
    for i in range(len(title1)-length+1):
        slice1 = title1[i:i+length].lower()
        for j in range(len(title2)-length+1):
            slice2 = title2[j:j+length].lower()
            if slice1 == slice2:
                #print(f"'{slice1}', '{slice2}'")
                matches += 1
                largest_slice = slice1
                slice1_index = i
                slice2_index = j

if matches:
    print(f"Number of matching substrings in phrases: {matches}")
    print(f"Longest substring in phrases: '{largest_slice}'")
    print(f"Index of the largest matching substring in phrase 1: {slice1_index}")
    print(f"Index of the largest matching substring in phrase 2: {slice2_index}")
else:
    print(f"No matching substrings.")