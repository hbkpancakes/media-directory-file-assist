# Media Directory File Assist, a bulk media file renamer by hbk Pancakes
https://twitter.com/hbkpancakes | hbkpancakes@protonmail.com

Media Directory File Assist is a script designed to help rename media files (specifically, TV Shows and Movies), so that Plex can automatically update the meta data (show/movie cover art, ratings, descriptions, episode names, etc).

# Requirements
- Python 3.x
- Windows 10

# Terminology
- Multi Files (or "Multi Episodes"): TV episodes that are joined together, for example, Episode 1 and 2 are in one.mp4 file (ShowName-E01E02)

# Setup and Instructions
Setup is fairly simple. Just run the script and you are good to go! Once you run it, you will be greeted to the main menu:

- Option 1: The TV Episode process. There are multiple choices you can make within this option:
  + Standard episode renaming: 
    + The files in your specified folder will instantly change
  + Multi episode renaming:
    + When declaring "Y" to "Are there multi episodes?", you will be asked to specify if all episodes are multi episodes or not
    + If only some episodes are joined, you can simply enter the number of "multi episodes" there are
    + The next prompt correspond to the number of "multi episodes" you decalred. You will be asked for the "First" and "Second" episodes of each joined file
- Option 2: The Movie process. There is only one option with 2 prompts: specifying movie name and year of release

NOTE: If you ever make a mistake, you can always revert your changes by responding "N" to the "Would you like to save changes?" prompt

# Contact Information 
https://twitter.com/hbkpancakes
https://github.com/hbkpancakes
hbkpancakes@protonmail.com
