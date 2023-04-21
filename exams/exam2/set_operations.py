# set_operations program

specs1 = {"core", "ram", "cpu"}
specs2 = {"ram", "bios", "cpu", "os"}

# Write the missing set operations on the four lines below
set_operation_1 = specs1.union(specs2)
set_operation_2 = specs1.intersection(specs2)
set_operation_3 = specs1.difference(specs2)
set_operation_4 = specs1.symmetric_difference(specs2)

if __name__ == "__main__":
    print(f"Set operation 1: {set_operation_1}")
    print(f"Set operation 2: {set_operation_2}")
    print(f"Set operation 3: {set_operation_3}")
    print(f"Set operation 4: {set_operation_4}")
