#
# Sylvia Chin
#
# Reads ISBN numbers from a data file then sorts it into sections
    # Valid ISBNs and Invalid ISBNs in a new output file
    
def main():
    # Welcome user to program
    print("Welcome to the ISBN validator program.")

    # Instruct user to input the file name with ISBN numbers
    infname = input("Please enter the name of the file with the ISBN numbers: ")

    # Instruct user to input the file name to output and sort ISBN numbers
    outfname = input("Please enter the name of the file to output and sort ISBN numbers: ")

    # Open the file of numbers to read it ("r") and save to variable 'infile'
    infile = open(infname, "r")

    # Open the output file to write in it ("w") and save to variable 'outfile'
    outfile = open(outfname, "w")

    # Save reading the file lines in a variable 'readinfile' so you can test
        # for both empty and for valid ISBNs
    readinfile = infile.readlines()

    # Check if the file is empty by checking if the variable 'readinfile'
        # returns an empty list
    if readinfile == []:
        # Print an error message
        print("Error: empty file. Please try again.")
        # End the program
        quit()

    # Create an empty list called 'valid' to store all valid ISBNs
    valid = []
    # Create an empty list called 'invalid' to store all invalid ISBNs
    invalid = []

    # Process each line of the file of 'readinfile' (reading file lines)
    for line in readinfile:
        # Create an empty list 'list_line' for each character of each line
        list_line = []
        # Create a counter 'numofch' to determine the number of characters
            # per line (per ISBN)
        numofch = 0
        # Use a for loop to iterate through every character in the line
            # excluding the newline character
        for i in line[:-1]:
            # Add one to the character counter
            numofch += 1
            # Add the character to the list 'list_line'
            list_line += i

        # Check if the character count is 10 characters
        if numofch == 10:
            # Initialize a variable called 'noletters' to indicate whether
                # there are characters other than numbers 0-9 in
                # characters 1-9
            noletters = 0
            # Use a for loop to iterate through characters indexes 0-8
            for i in list_line[0:9]:
                # If the characters are not 0-9
                if not (i == "0" or i == "1" or i == "2" or i == "3" or i ==
                        "4" or i == "5" or i == "6" or i == "7" or i == "8"
                        or i == "9"):
                    # Save the line excluding the newline character and
                        # concatenated with the appropriate error message
                        # to variable 'str_line'
                    str_line = (line[:-1] + " ; invalid 1st-9th character")
                    # Append str_line to the invalid list 'invalid'
                    invalid.append(str_line)
                    # Let 'noletters' be 1
                    noletters = 1
            # Check if the 10th character is 0-9 or X
            if (list_line[9] == "X" or list_line[9] == "0" or
                list_line[9] == "1" or list_line[9] == "2" or
                list_line[9] == "3" or list_line[9] == "4" or
                list_line[9] == "5" or list_line[9] == "6" or
                list_line[9] == "7" or list_line[9] == "8" or
                list_line[9] == "9"):
                # If the 10th character is X, equate that to 10
                if list_line[9] == "X":
                    list_line[9] = 10
                # If 'noletters' is still 0, meaning it does not carry
                    # an invalid character in positions 1-9
                if noletters == 0:
                    # Check if the characters satisfy the ISBN equation
                        # Convert each to integers
                    if (((int(list_line[0])*10 + int(list_line[1])*9 +
                        int(list_line[2])*8 + int(list_line[3])*7 +
                        int(list_line[4])*6 + int(list_line[5])*5 +
                        int(list_line[6])*4 + int(list_line[7])*3 +
                        int(list_line[8])*2 + int(list_line[9])) %
                         11) == 0):
                        # If so, append the line excluding the newline
                            # character to the valid list 'valid'
                        valid.append(line[:-1])
                    # If the line doesn't satisfy the ISBN equation
                    else:
                        # Add an appropriate error message to end of the
                            # line
                        str_line = (line[:-1] +
                                    " ; invalid equation result")
                        # Append concatenated string to list 'invalid'
                        invalid.append(str_line)
            # If the 10th character is not 0-9 or X
            else:
                # Add an appropriate error message to end of the
                    # line
                str_line = (line[:-1] + " ; invalid 10th character")
                # Append concatenated string to list 'invalid'
                invalid.append(str_line)
        # If the number of characters is not 10
        else:
            # Add an appropriate error message to end of the
                # line
            str_line = (line[:-1] + " ; invalid number of characters")
            # Append concatenated string to list 'invalid'
            invalid.append(str_line)

    # Write the first line of the outfile to be 'Valid ISBNs'
    print("Valid ISBNs", file=outfile)

    # Use a for loop to check each item in the valid list
    for i in valid:
        # Print each item to the outfile in a new line
        print(i, file=outfile)

    # Add an extra space in between valid and invalid ISBNs
    print("\n", file=outfile)

    # Write the header for 'Invalid ISBNs' to the outfile
    print("Invalid ISBNs", file=outfile)

    # Use a for loop to check each item in the invalid list
    for i in invalid:
        # Print each item to the outfile in a new line
        print(i, file=outfile)

    # Print a message in the shell to let user know the sorting is complete
    print("Sorted! Please check your output file for the results.")    

    # Close both files
    infile.close()
    outfile.close()
