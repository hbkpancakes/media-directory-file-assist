# Media Directory File Assist v1.0
# Edits file names in directory for easy import to media server

import os, getpass
from sys import exit

# Welcome message
print("Media Directory File Assist v1.0\n")
user = getpass.getuser()
print('Welcome, ' + user + '\n')

while True:
    print("What type of files are you trying to change?\n")
    print("1. TV Shows\n2. Movies\n\n0. Exit\n")

    # Starts entry too loop to ensure accurate input
    while True:
        user_choice = input('Choice: ')
        if user_choice in ('1', '2', '0'):
            break
        print("\nInvalid input. Please enter a number corresponding to the option to wish to use.\n")
    # If user enters correct response
    if user_choice == '1':

        while True:
            # Checks to make sure user is entering a valid directory
            found = False
            filenamedir = None
            while not found:
            # Defines user input to locate file directory and show info
                filenamedir = input("\nFile path directory? ")
                if filenamedir == '/exit':
                    exit()
                elif not os.path.isdir(filenamedir):
                    print("\n" + filenamedir + " " "is not a valid directory\n")
                else:
                    print("\nUser specified directory: " + filenamedir)
                    found = True

            path = os.getcwd()
            os.chdir(filenamedir)
            filenames = os.listdir(filenamedir)
            
            # Gathers show name and season to store for renaming
            while True:
                showname = input("\nWhat is the show name? ")
                if showname == '/exit':
                    exit()
                season = input("What season are you renaming? ")
                if season == '/exit':
                    exit()
                # Start of special character error handling
                try:
                    # Handles multi episode files
                    while True:
                        epid = str.casefold(input("Are there multi episodes (ex. 'S01E01E02')? [Y/N]: "))
                        if epid == '/exit':
                            exit()
                        elif epid in ('y', 'n'):
                            break
                        print("Invalid input. Please enter 'Y' OR 'N'.")
                    if epid == 'y':
                        while True:   
                            multicheck = str.casefold(input("Are all episodes multi episode? [Y/N]: "))
                            if multicheck == '/exit':
                                exit()
                            elif multicheck in ('y', 'n'):
                                break
                            print("Invalid input. Please enter 'Y' OR 'N'.")
                        if multicheck == 'y':
                            # Starts renaming loop if user specifies all episodes are multi episode files
                            path = os.getcwd()
                            os.chdir(filenamedir)
                            filenames = os.listdir(filenamedir)
                            COUNT = 1
                            oldnames = []

                            for f in filenames:
                                f_name, f_ext = os.path.splitext(f)
                                if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ".jpg", ".sfv", ""):
                                    f_name = showname + " - " + "S" + season.zfill(2) + "E" + str(COUNT).zfill(2) +  "E" + str(COUNT+1).zfill(2)
                                    COUNT = COUNT + 2

                                new_name = '{}{}'.format(f_name, f_ext)
                                os.rename(f, new_name)
                                oldnames.append(new_name)
                        
                        # Starts renaming loop if user specifies only some episodes are multi episode, gathering # of occurrences and stores those episodes in lists
                        else:
                            eplista = []
                            eplistb = []
                            while True:
                                epstochange = input("How many multi eps? ")
                                try:
                                    if epstochange == '/exit':
                                        exit()
                                    elif int(epstochange) < len(filenames):
                                        break
                                    print("\nYou specified more files than are actually in the file directory. Please make sure you specify " + str(len(filenames)) + " or less files.\n")
                                except ValueError:
                                    print('\nEntry must be a number or "/exit". Please try again.\n')
                            for i in range(int(epstochange)):
                                i += 1
                                print("\nWhich episodes are joined?")
                                eptokea = input("First Episode: ")
                                if eptokea == '/exit':
                                    exit()
                                eptokeb = input("Second Episode: ")
                                if eptokeb == '/exit':
                                    exit()
                                eplista.append(eptokea)
                                eplistb.append(eptokeb)
                            
                            # Starts loop if user specifies tv shows are multi episode
                            path = os.getcwd()
                            os.chdir(filenamedir)
                            filenames = os.listdir(filenamedir)
                            COUNT = 1
                            oldnames = []

                            i = 0
                            for f in filenames:
                                f_name, f_ext = os.path.splitext(f)
                            
                                # Changed WHILE to IF and added check for i
                                if i < len(eplista) and str(COUNT) == eplista[i]:
                                    if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ".jpg", ".sfv", ""):
                                        # Removed list comprehension to perform zero fill
                                        # Instead added to the formatted string
                                        f_name = showname + " - " + "S" + season.zfill(2) + "E" + eplista[i].zfill(2) + "E" + eplistb[i].zfill(2)
                                        COUNT = COUNT + 2 # Changed inline function
                    
                                    new_name = '{}{}'.format(f_name, f_ext) # Removed space
                                    os.rename(f, new_name)
                                    oldnames.append(new_name)
                                    i += 1 # Assigned incremented value
                
                                else:
                                    if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ".jpg", ".sfv", ""):
                                        f_name = showname + " - " + "S" + season.zfill(2) + "E" + str(COUNT).zfill(2)
                                        COUNT = COUNT + 1 # Changed inline function
                                    new_name = '{}{}'.format(f_name, f_ext) # Removed space
                                    os.rename(f, new_name)
                                    oldnames.append(new_name)

                    # Starts renaming loop if user specifies files are not multi episode
                    else:
                        path = os.getcwd()
                        os.chdir(filenamedir)
                        filenames = os.listdir(filenamedir)
                        COUNT = 1
                        oldnames = []

                        for f in filenames:
                            f_name, f_ext = os.path.splitext(f)
                            if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ".jpg", ".sfv", ""):
                                f_name = showname + " - " + "S" + season.zfill(2) + "E" + str(COUNT).zfill(2)
                                COUNT = COUNT + 1

                            new_name = '{}{}'.format(f_name, f_ext)
                            os.rename(f, new_name)
                            oldnames.append(new_name)
                
                # End of special character error handling
                except WindowsError as er:
                    if er.winerror == 123:
                        print("\nSpecial characters cannot be used in file names (ex. '!', '?', etc). Please try again.")
                else:
                    break

            # Ending message, saving flag, and option to loop through program again
            print("\nChange complete")

            while True:
                savecheck = str.casefold(input("\nWould you like to save changes? [Y/N] "))
                if savecheck in ('y', 'n'):
                    break
                print("\nInvalid input. Please enter 'Y' OR 'N'.")
            if savecheck == 'n':
                i = 0
                COUNT = 1
                for fr in filenames:
                    f_name, f_ext = os.path.splitext(f)
                    if i < len(filenames):
                        f_name_restore = filenames[i]
                        COUNT = COUNT + 1
                
                        name_restore = '{}'.format(f_name_restore)
                        os.rename(oldnames[i], f_name_restore)
                        i += 1 # Assigned incremented value
        
            # Continue program or end
            while True:
                answer = str.casefold(input('\nRun again? [Y/N]: '))
                if answer in ('y', 'n'):
                    break
                print("Invalid input. Please enter 'y' OR 'n'.")
            if answer == 'y':
                continue
            else:
                print("\nReturning to home...\n")
                break        

    if user_choice == '2':

        while True:
            # Checks to make sure user is entering a valid directory
            found = False
            filenamedir = None
            while not found:
            # Defines user input to locate file directory and show info
                filenamedir = input("\nFile path directory? ")
                if filenamedir == '/exit':
                    exit()
                elif not os.path.isdir(filenamedir):
                    print("\n" + filenamedir + " " "is not a valid directory\n")
                else:
                    print("\nUser specified directory: " + filenamedir)
                    found = True

            path = os.getcwd()
            os.chdir(filenamedir)
            filenames = os.listdir(filenamedir)

            while True:
                movie_name = input("\nWhat is the movie name? ")
                if movie_name == '/exit':
                    exit()
                release_year = input("What is the year of release? ")
                if release_year == '/exit':
                    exit()
                # Start of special character error handling
                try:

                    path = os.getcwd()
                    os.chdir(filenamedir)
                    filenames = os.listdir(filenamedir)
                    COUNT = 1
                    oldnames = []

                    for f in filenames:
                        f_name, f_ext = os.path.splitext(f)
                        if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ".jpg", ".sfv", ""):
                            f_name = movie_name + " (" + release_year + ")"
                            COUNT = COUNT + 1

                        new_name = '{}{}'.format(f_name, f_ext)
                        os.rename(f, new_name)
                        oldnames.append(new_name)
                        
                except WindowsError as er:
                    if er.winerror == 123:
                        print("\nSpecial characters cannot be used in file names (ex. '!', '?', etc). Please try again.")
                else:
                    break
            
            # Ending message, saving flag, and option to loop through program again
            print("\nChange complete")

            while True:
                savecheck = str.casefold(input("\nWould you like to save changes? [Y/N] "))
                if savecheck in ('y', 'n'):
                    break
                print("\nInvalid input. Please enter 'Y' OR 'N'.")
            if savecheck == 'n':
                i = 0
                COUNT = 1
                for fr in filenames:
                    f_name, f_ext = os.path.splitext(f)
                    if i < len(filenames):
                        f_name_restore = filenames[i]
                        COUNT = COUNT + 1
                
                        name_restore = '{}'.format(f_name_restore)
                        os.rename(oldnames[i], f_name_restore)
                        i += 1 # Assigned incremented value

            # Continue program or end
            while True:
                answer = str.casefold(input('\nRun again? [Y/N]: '))
                if answer in ('y', 'n'):
                    break
                print("Invalid input. Please enter 'y' OR 'n'.")
            if answer == 'y':
                continue
            else:
                print("\nReturning to home...\n")
                break
    
    if user_choice == '0':
        exit()
