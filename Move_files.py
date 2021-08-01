# Import the following modules
import os
import time
import shutil
import datetime
import glob
  
  
# Change the directory and jump to the location
# where you want to arrange the files
os.chdir(r"C:\Users\Dell\Downloads\FireShot")
  
# List the directories and make a list
all_files = list(os.listdir())
  
# Get the current working directory
outputs = os.getcwd()
  
# Run a loop for traversing through all the 
# files in the current directory
for files in all_files:
    try:
        
        # Jump to the directories files
        inputs = glob.glob(files+"\\*")
          
        # Now again run a loop for travering through
        # all the files inside the folder
        for ele in inputs:
            
            # Now, move the files one-by-one
            shutil.move(ele, outputs)
          
        # After extracting files from the folders, 
        # delete that folder
        shutil.rmtree(files)
    except:
        pass
  
# Again run a loop for traversing through all the
# files in the current directory
for files in os.listdir('.'):
      
    # Get all the details of the file creation 
    # and modification
    time_format = time.gmtime(os.path.getmtime(files))
      
    # Now, extract only the Year, Month, and Day
    datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
      
    # Provide the number and find the month
    full_month_name = datetime_object.strftime(
        "%b")
      
    # Give the name of the folder
    dir_name = full_month_name + '-' + \
        str(time_format.tm_mday) + "-" + \
        str(time_format.tm_year)
  
    # Check if the folder exists or not
    if not os.path.isdir(dir_name):
         
        # If not then make the new folder
        os.mkdir(dir_name)
    dest = dir_name
      
    # Move all the files to their respective folders
    shutil.move(files, dest)
      
print("Suceessfully moved...")
