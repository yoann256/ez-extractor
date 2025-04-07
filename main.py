###################################################################
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |   Program written by        #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |   @yoann256 on GitHub.      #
# %%%%%%%%%%%%%%%%%%::%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%#%%*.%%#%%%%%%%%    |                             # 
# %%%%%%%#-..:%##%#.#%%*...+%%%%    |   You can remove those      #
# %%%%#..=%%%%%#%%.=###%%%%%=..%    |   lines when redistributing #
# %##%%%#:..=%#%%-.%%%%%#:..-%%%    |   this project.             #
# %%####%%%##.%%#.%%%##==%%%%%%%    |                             #
# %%%%%%%%%%##%%.*%#%%%%%%%%%%%%    |                             #
# %%%%%%%%%%#%%%%%%%%%%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |                             #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |   MIT License 2025          #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    |                             #
###################################################################

import zipfile
import os.path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


fileName = input("Please enter the file path: ") 
print("File checking, please wait...")

# Checks if file exists
if not os.path.isfile(fileName):
    print(f"{bcolors.FAIL}Error: This file does not exist!{bcolors.ENDC}")
    quit()

# Checks if file is an archive
if not zipfile.is_zipfile(fileName):
    print(f"{bcolors.FAIL}Error: This file is not an archive!{bcolors.ENDC}")
    quit()

extractDir = input("Select a directory to extract the archive contents to: ")

if not os.path.exists(extractDir):
    createDir = input("Directory not found, create it? (Y/N): ")

    if createDir == "Y" or createDir == "y":
        os.makedirs(extractDir)
    else:
        print("Can't extract. Aborted.")
        quit()

zipFile = zipfile.ZipFile(fileName, "r")

# To-do: Include this feature
# print("Select an extract option:")
# print("N - Extract into the specified directory without creating another directory")
# print("D - Extract in another directory within the selected directory")

# extractOption = input("Select an option (N/D): ")

# if extractOption == "D":
#     extractDir = fileName

zipFile.extractall(extractDir)