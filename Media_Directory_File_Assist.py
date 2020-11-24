# Media Directory File Assist v1.0
# Edits file names in directory for easy import to media server

import os, getpass, movie_option, tv_show_option
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
        tv_show_option.tv_show_rename()
    if user_choice == '2':
        movie_option.movie_rename()
    if user_choice == '0':
        exit()