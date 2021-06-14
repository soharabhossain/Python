#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------
# Read from a Text File
#-------------------------------------------
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Read the content Line-By-Line
#---------------------------------
# Open the file in 'read' mode
file1 = open('Input_File.txt', 'r')

# Read all the lines if the file using readlines()
# This will sotre all the lines as a list
all_lines = file1.readlines()
print(all_lines) 

# Now process the lines one-by-one
# We would like to check the content of the file line-by-line
count = 0


print('\n\n Processing the file line-by-line : ')
# Strips the newline character
for line in all_lines:
    count += 1
    print(" Line{} -> {}".format(count, line.strip()))
 
file1.close()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------
# Read the entire content at a time
#-------------------------------------------

# Open the file in 'read' mode
file1 = open('Input_File.txt', 'r')

# Read the entire content of the file
entire_file_content = file1.read()

print('\n\n Display the entire file : ')
print(entire_file_content) 

# Close the file
file1.close()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------
# Read the partial content of the file
#-------------------------------------------

# Open the file in 'read' mode
file1 = open('Input_File.txt', 'r')

# Read only 10 bytes of data from the file
# 1 byte = 1 character (for a text file)
partial_content = file1.read(20)

print('\n\n Display the partial content : ')
# Print all the lines - print the list
print(partial_content) 

# Close the file
file1.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# --------------------- WRITE ------------------------
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

print("\n\n Write to a file....")

#-------------------------------------------
# Write to a Text File
#-------------------------------------------

# Write content in a file line-by-line 

# Open the file in 'write' mode
file2 = open('Output_File.txt', 'w')

while True:
    line_of_text = input("Enter a line (type \'done\' to end): " )
    if line_of_text=='done':
        break
    
    file2.write(line_of_text + "\n")

# Close the file
file2.close()


# Now open the file in 'Read' mode and display the entire content
file2 = open('Output_File.txt', 'r')
file_buffer = file2.read()

print('\n The content of the file is as follows: ')
print(file_buffer)

# Close the file
file2.close()


#-------------------------------------------
# Append/Write to a Text File
#-------------------------------------------

print("\n\n Append in the file....")

#-------------------------------------------
# Append/Write to a Text File
#-------------------------------------------

# Write content in a file line-by-line 

# Open the file in 'append' mode
file2 = open('Output_File.txt', 'a')

while True:
    line_of_text = input("Enter a line (type \'done\' to end): " )
    if line_of_text=='done':
        break
    
    file2.write(line_of_text + "\n")

# Close the file
file2.close()


# Now open the file in 'Read' mode and display the entire content
file2 = open('Output_File.txt', 'r')
file_buffer = file2.read()
print('\n The content of the file is as follows: ')
print(file_buffer)

# Close the file
file2.close()





