import os
import sys.argv
import os.path

def getfolderallname(path):
	folder_file = open('laiyue_foldername.txt', 'w')
	for parent,dirnames,filenames in os.walk(path):
		for dirname in dirnames:
			folder_file.write(dirname + '\n')
	folder_file.close()

		   	
if __name__ == "__main__":
	getfolderallname(sys.argv[1])
	target_file = open('laiyue_target_file.txt','w')
	for foldername in open('laiyue_foldername.txt', 'r').readlines():
		if '_' in foldername:
			date = foldername.split('_')[argv[2]]
			if int(sys.argv[3]) >= int(date):
				target_file.write(foldername)
	target_file.close()


	