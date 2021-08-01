![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/Move_files_according_to_date?color=red&label=Repo%20Size%20)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatyam/Move_files_according_to_date?color=red&label=Lines%20of%20Code)</br>
![sds](https://profile-counter.glitch.me/{Move_files_according_to_date}/count.svg)


Build a Python script that would move all of your files to new directories based on their creation and modification dates. Basically, it will look for directories and, if any are found, it will extract all the files from that folder, delete that folder, and then arrange them by creation date.

## Approach: 

- To change the directory and move to the directory where you wish to place all your files based on the modification date, use the ***os.chdir*** function.
- To list all the folders and files, use the ***os.listdir*** function.
- To get the current working directory, use the ***os.getcwd*** method.
- Run a loop to go over all the files within and outside the directories.
- For storing all the file instances, use the glob.glob function. It will take the file name or file path and search for all the files present inside it.
- We may simply move files from one location to another by using the shutil.move method. Pass the file name which is to be moved and the path where to be moved.
- After removing the files from the folder, use the shutil.rmtree methods to remove the folder. Pass the file name to be removed in ***shutil.rmtree*** function.
- Set a loop once more to go through all the files.
- Use ***time.gmtime*** to retrieve all the data about a file’s creation and modifications in the structural form.
- Then, one by one, extract the ***Year***, ***Month***, and ***Day***.
- Run an If condition to see if that folder has already been created; if not, create it using the file’s creation date as the name.
- Finally, using the ***shutil.move*** function, move all the files one by one to the newly formed folder.
- Read complete article [**here**](https://www.geeksforgeeks.org/python-move-files-to-creation-and-modification-date-named-directories/)

## Output: 
### Before:
<img width="696" alt="1" src="https://user-images.githubusercontent.com/69134468/127762342-13a1383b-a7c0-4aae-bffc-4a32d324dfe5.PNG">

### After: 
<img width="694" alt="2" src="https://user-images.githubusercontent.com/69134468/127762340-cc73f2e5-fac7-4b3c-8dc2-9ab5346a1c9f.PNG">
