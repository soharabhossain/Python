# Usage of the code from the command prompt
# python CMD_line_Args.py -- help
# python CMD_line_Args.py -n Soharab -s Shaikh
# python CMD_line_Args.py -n Soharab

#------------------------------------------------
# import the necessary packages
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

# Mandatory argument
ap.add_argument("-n", "--name", required=True, help="name of the user")
# Optional argument
ap.add_argument("-s", "--surname", required=False, help="Surname of the user")

args = vars(ap.parse_args())
 
# display a friendly message to the user
print("Hi {}, how are you?".format(args["name"]))

# If the argument is specified
if args["surname"]:
    print(args["surname"])
else:
    print('Surname not mentioned.!!!') # If the argument is not specified



