# Media Directory File Assist v1.0 - Movie Option
# Movie Option: Allows user to change the name of a single movie file 

def movie_rename():
    import os, getpass

    # Welcome message
    print("\nMedia Directory File Assist - Movies\n")
    print("Please consult the README if you have any questions.\n")

    # Start program (while loop for continous loop through program if user chooses to run again)
    while True:

        # Checks to make sure user is entering a valid directory
        found = False
        filenamedir = None
        while not found:
        # Defines user input to locate file directory and show info
            filenamedir = input("File path directory? ")
            if not os.path.isdir(filenamedir):
                print("\n" + filenamedir + " " "is not a valid directory\n")
            else:
                print("\nUser specified directory: " + filenamedir)
                found = True

        path = os.getcwd()
        os.chdir(filenamedir)
        filenames = os.listdir(filenamedir)

        while True:
            movie_name = input("\nWhat is the movie name? ")
            release_year = input("What is the year of release? ")
            # Start of special character error handling
            try:

                path = os.getcwd()
                os.chdir(filenamedir)
                filenames = os.listdir(filenamedir)
                COUNT = 1
                oldnames = []

                for f in filenames:
                    f_name, f_ext = os.path.splitext(f)
                    if f_ext not in (".txt", ".srt", ".nfo", ".dat", ".exe", ""):
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