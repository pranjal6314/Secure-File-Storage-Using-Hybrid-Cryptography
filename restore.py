import sys
import os, shutil  # import os and shutil modules , 
import tools

def restore():
	tools.empty_folder('restored_file') 

	chapters = 0 
	
	meta_data = open('raw_data/meta_data.txt','r') # open meta_data.txt file in raw_data folder
	meta_info = [] # used to store meta data of file  , meta_info[0] = file name , meta_info[1] = total chapters , meta_info[2] = file size
	for row in meta_data: # loop through each line in meta_data.txt file
		temp = row.split('\n') 
		temp = temp[0] 
		temp = temp.split('=')
		meta_info.append(temp[1]) # append data in meta_info list
	address = 'restored_file/' + meta_info[0]  # address of restored file
	
	list_of_files = sorted(tools.list_dir('files')) # get list of files in files folder , these files are divided files of main file

	with open(address,'wb') as writer: # open file in write binary mode
		for file in list_of_files: # loop through each file in files folder
			path = 'files/' + file # get path of file
			with open(path,'rb') as reader: # open file in read binary mode
				for line in reader: # loop through each line in file
					writer.write(line) # write data in file , this file is restored file
				reader.close()
		writer.close()

	tools.empty_folder('files')