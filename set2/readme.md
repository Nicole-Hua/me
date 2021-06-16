Updated official email from zid to name
Updated the tests for sets
python ../course/set2/tests.py
() means that it is a string
.upper or .lower to make the string either in upper or lowercase
str() function converts the specified value into a string
Plus sign (+) can add more to the string adding a number or character after the string (e.g. a_string.upper() + "!" will make the string upper case and with an !)
This " " creates a space between letters/ characters
To debug the syntax errors run the script and it will show you were the errors are in the terminal to fix
This == means equal
This len means length
elif means else if
.append() adds to the end of a list
Watch the indentation if there is a syntax error that isn't obvious
For Loop twice to create a list within a list like a branching system
loops_3 exercise - listrow = [] Creates a new list for the rows, for j in range(10): give the rows a range like the beginning, append the i because it remains the same throughout the list whereas the j range will increase by 1 each time, listnumber.append(listrow) - Loops the listnumber by the row to create the rising block of numbers
loops_4 exercise - Similar to Loops_3 exercise however changed only i to j as we want an ascending list to be looped in rows
loops_5 exercise - same as loops_3 exercise however when we append the list for the row we put this in the ("(i" + str(i) + ", j" + str(j) + ")") = (i0, j0)
^ Another method of doing this without all the +s is to format the coordinates with curly brackets {} - cordrow.append(f"(i{i}, j{j})") so that it knows where the place the i values and j values into the coordinate format.
loops_6 exercise - similar to loops_3 exercise however we change the range for j from 10 to i [as i controls the range of rows of lists going down]
loops_7 exercise -
