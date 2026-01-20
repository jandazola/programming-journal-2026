from christmas_tree import build_christmas_tree
import os

# get tree size from user
while True:
    try:
        tree_size = int(input('Enter tree size: '))
    # catches ValueError if entered value is not numerical
    except ValueError:
        print('Please enter a numerical value.')
        continue
    else:
        break

# get count of ornaments from user
while True:
    try:
        prompt = 'Enter the number of different oranments you would '
        prompt += 'like for your tree: '
        ornament_count = int(input(prompt))
    # catches ValueError if entered value is not numerical
    except ValueError:
        print('Please enter a numerical value.')
        continue
    else:
        break

# build list to house entered ornaments
ornament_list = []

# loops for the amount of ornaments the user selected
while ornament_count > 0:
    # ask for ornament
    prompt = 'Enter a single character ornament you would like '
    prompt += 'to use for your tree: '
    ornament = input(prompt)

    # conditional to ensure entered option is a single character
    if len(ornament) > 1:
        print('Remember to enter a single character as an ornament.\n')
        # returns back to the top of the loop
        continue
    else:
        # adds ornament to list
        ornament_list.append(ornament)

    # reduces the count of ornaments (loop iterations) by 1 and loops
    #  again (or ends the loop if zero)
    ornament_count -= 1

# convert list to tuple to use as arbitrary (variable length) arugment
#  in build_christmas_tree function
ornaments = tuple(ornament_list)

# build tree
tree = build_christmas_tree(tree_size,*ornaments)

# writes the created tree to a separate file, also creates the file
#  if it doesn't exist yet 
filename = 'christmas_tree.txt'
with open(filename, 'w') as f:
    f.write(tree)

# gets the current working directory the user is working in
current_dir = os.getcwd()

# prints where (the file path) the user can find their tree file at
print(f'\nYour {filename} file can be found at: {current_dir}.')