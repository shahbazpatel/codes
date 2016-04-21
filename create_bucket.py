from subprocess import call as s_call 
#subprocess.call()--> takes input as subprocess.call(["ls","-l"]) command as a list

import sys #for sys.exit() Program termination


ch=int() #ch will be of type integer

while(ch!=8):
	print "\nMenu"
	print "1.Create Bucket"
	print "2.Delete Bucket"
	print "3.Download File"
	print "4.Upload File "
	print "5.Delete File"
	print "6.View Buckets"
	print "7.View Bucket contents"
	print "8.EXIT"
	while(1):	
		#try-except block for invalid input by user 
		try:		
			ch=int(raw_input("Enter your choice: \n"))
			break #come out of loop after valid input
	
		except ValueError: #ValueError is a type of exception
			pass #don't do anything
	if ch==1:
		bucket=raw_input("Enter bucket name:\n")
		region=raw_input("Enter region name:\n")
		cmd="aws s3api create-bucket --bucket %s --region %s"%(bucket,region) # replace '%s' with proper values
		print 'command : ', cmd,'\n', 'using split() : ',cmd.split() #print the whole command
		s_call(cmd.split()) # split and give it as a list to subprocess.call() i.e s_call()

	elif ch==2:	
		bucket=raw_input("Enter bucket name:\n")
		region=raw_input("Enter region name:\n")
		cmd="aws s3api delete-bucket --bucket %s --region %s"%(bucket,region)
		print 'command : ', cmd
		s_call(cmd.split())

	elif ch==3:	
		src_path=raw_input("Enter File path: 'From s3 to local : eg. /<bucket_name>/<folder_name>/...'\n")
		dest_path=raw_input("Enter Destination path:\n")
		cmd="aws s3 cp s3:/%s %s"%(src_path,dest_path)
		print 'command : ', cmd
		s_call(cmd.split())

	elif ch==4:	
		src_path=raw_input("Enter File path: 'From local to s3 storage'\n")
		dest_path=raw_input("Enter Destination path: 'eg. /<bucket_name>/<folder_name>/...'\n")
		cmd="aws s3 cp %s s3:/%s"%(src_path,dest_path)
		print 'command : ', cmd
		s_call(cmd.split())

	elif ch==5:	
		file_path=raw_input("Enter File path to be deleted: 'eg. /<bucket_name>/<folder_name>/<file_name>...'\n")
		cmd="aws s3 rm s3:/%s"%(file_path)
		print 'command : ', cmd		
		s_call(cmd.split())

	elif ch==6:
		cmd="aws s3 ls"
		print 'command : ', cmd
		s_call(cmd.split())

	elif ch==7:
		bucket=raw_input("Enter the bucket name:\n")
		cmd="aws s3 ls %s"%bucket
		print 'command : ', cmd		
		s_call(cmd.split())

	elif ch==8:
		print "Exited!"
		sys.exit()
	else:
		print "Enter correct choice!"
