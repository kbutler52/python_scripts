#!/bin/bash 
#This is a required header for linux scripts 

#The purpose of this linux script is to introduce linux scripting
#Linux scripting or shell scripting (as far as I'm aware) is used to 
#Combine multiple linux commands into a single executable file

cd #Like usual, this command will go root folder
cd Desktop #This will go to desktop folder
mkdir ScriptCreatedFolder #This will create a folder on the desktop named 'ScriptCreatedFolder

#These are all linux commands you already know, all you're doing is putting them into a .sh or shell file

#cd here just 'visits' the folder, you will still 'live' in the folder you executed the file from
#unless you use . ./FirstLinuxScript.sh but don't worry about that right now. 

cd ScriptCreatedFolder #while 'visiting' the Desktop folder, 'visit' the newly created ScriptCreatedFolder 

cat > pythonReview.py <<- "EOF" 
print("You just made your first linux script")#This is a standard print statement in python
EOF
#Creates a python file called pythonReview.py and uses the string "EOF" to close the file
#dont worry about knowing <<- "EOF" I googled that
#This is where EOF or End Of File is used in linux to close the cat statement