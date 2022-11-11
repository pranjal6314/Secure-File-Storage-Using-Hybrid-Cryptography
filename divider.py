import sys
import tools

def divide(): # divide file into 1MB chunks
	tools.empty_folder('files')
	tools.empty_folder('raw_data')
	FILE = tools.list_dir('uploads')
	FILE = './uploads/'+FILE[0]

	MAX  = 1024*32	 # max size of each file in bytes , 1MB = 1024*1024 bytes , 32KB = 1024*32 bytes
						# 1	MB	-	max chapter size
	BUF  = 50*1024*1024*1024  			# 50GB	-	memory buffer size

	chapters = 0  #used for naming the files
	uglybuf  = ''  # used for storing the last chunk of data
	meta_data = open('raw_data/meta_data.txt','w') # create meta_data.txt file in raw_data folder , used to store meta data of file
	file__name = FILE.split('/') 
	file__name = file__name[-1] 
	print (file__name)
	meta_data.write("File_Name=%s\n" % (file__name)) # write file name in meta_data.txt file
	with open(FILE, 'rb') as src: # open file in read binary mode
		while True:
			target_file = open('files/SECRET' + '%07d' % chapters, 'wb') # open file in write binary mode
			written = 0 # used for counting bytes written in each file
			while written < MAX: # loop until written bytes are less than max chapter size
				if len(uglybuf) > 0: 
					target_file.write(uglybuf) # write data in file
				target_file.write(src.read(min(BUF, MAX - written))) # write data in file , min(BUF, MAX - written)` is used to avoid reading more than max chapter size
				written += min(BUF, MAX - written) # update written bytes
				uglybuf = src.read(1) # read 1 byte from file ,this file is main file , not the target file ,given by user
				if len(uglybuf) == 0: # if no data is read
					break
			target_file.close() 
			if len(uglybuf) == 0: 
				break
			chapters += 1 # update chapter number
	meta_data.write("chapters=%d" % (chapters+1)) # write total chapters in meta_data.txt file
	meta_data.close()