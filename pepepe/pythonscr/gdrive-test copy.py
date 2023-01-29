from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import random


gauth = GoogleAuth()
gauth.CommandLineAuth()  
drive = GoogleDrive(gauth)

num = 0

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1tfBsDRhH5kTmq1Uz_SjggyZJvC74PHf3')}).GetList()

randNum = random.randint(0, len(file_list)-1)

for file in file_list:
	if num == randNum:
		file.GetContentFile(file['title'])
	num+=1

print(len(file_list))