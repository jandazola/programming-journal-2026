import os

### version 1 ###
# absolute_filepath = __file__
# current_filename = os.path.basename(absolute_filepath)
# length_with_ext = len(current_filename)
# filename = absolute_filepath[:-length_with_ext] + "dunder_variable_notes.txt"

### version 2 ###
length_with_ext = len(os.path.basename(__file__))
filename = __file__[:-length_with_ext] + "Week_04_Notes.txt"

### version 3 ###
# filename = __file__[:-len(os.path.basename(__file__))] + "Week_04_Notes.txt"

with open(filename) as f:
    lines = f.readlines()
    for i in range(1,4):
        print(lines[i][3:].strip())
    print()

print(f"The dunder variable __file__ for this file is {__file__}\n")

if __name__ == "__main__":
    print("This file_1.py is being run as the main program.")
    print(f"Thus, the __name__ variable for file_1.py is {__name__}")
else:
    print("This file_1.py is being run as an imported module.")
    print(f"Thus, the __name__ variable for file_1.py is {__name__}")
