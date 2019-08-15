# .txt to .py
# Handles conversion between master .txt file and outputs to a .py file
# First version: @daydreamjesse 8/14/19

with open("texttoscrape.txt", "r") as file:
    # Get data from .txt file
    lines = file.readlines()
    data = []
    # bool for control
    endFunc = False
    # start parsing text
    for item in lines:
        if endFunc == False:
            # detect a function definition
            if "def" in item:
                # breakdown the line to get function name
                breakdown = item.split()
                for obj in breakdown:
                    if "(" in obj:
                        # set the file name to name of function
                        fileName = obj.split("(")
                        newFile = (fileName[0] + ".py")
                        # end of first runthrough
                        endFunc = True
                        break
        # if a function has been detected
        elif endFunc == True:
            # if a nested function, start the process over on the next line
            if "def" in item:
                endFunc = False
                continue
            else:
                # store the code held in the function
                data.append(item)

# create a new .py file with function name
with open(newFile, "w") as file:
    # save function to new script
    file.writelines(data)
