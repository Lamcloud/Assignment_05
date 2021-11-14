#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SLam, 2021-Nov-13, Modified File
#------------------------------------------#

import os.path # to use exists function to check if file exists for loading

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Check if file exists
        if os.path.exists(strFileName) == True:
            # Load existing data if file exists
            lstTbl = []
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2].strip()}
                lstTbl.append(dicRow)
            objFile.close()
        # If file doesn't exist, tell user
        else:
            print('File', strFileName, 'does not exist.')
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table of dicts each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
        
    elif strChoice == 'd':
        # Delete an entry
        found = False
        cd = int(input('Enter CD number to delete: '))
        # If CD number is found in inventory, then delete it
        for row in lstTbl:
            if row['id'] == cd:
                lstTbl.remove(row)
                print('CD', cd, 'has been deleted.')
                found = True
                break
        # If CD number is not found, tell the user
        if found == False:
            print('CD', cd, 'is not in inventory.')
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') # overwrite file to prevent duplicating records
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')

