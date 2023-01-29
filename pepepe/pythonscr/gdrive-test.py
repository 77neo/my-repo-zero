from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()  
drive = GoogleDrive(gauth)

# Create a GoogleDriveFile instance with title 'test.txt'.
file1 = drive.CreateFile({'title': 'test.txt'})  
# Set content of the file from the given string.
file1.SetContentString('Hello World!') 
file1.Upload()

