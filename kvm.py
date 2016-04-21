from subprocess import call as s_call
import sys

ch=int()

while(ch!=13):
	print "menu"
	print "1.list"
	print "2.vcpucount"
	print "3.version"
	print "4.nodestat"
	print "5.system list"
	print "5.exit"
	
	while(1):
		try:
			ch=int(raw_input("enter choice\n"))
			break
		except ValueError:
			pass
	if ch==1:
		
		cmd="virsh list"
		s_call(cmd.split())
	if ch==2:
		cmd="virsh vcpucount ubuntu"
		s_call(cmd.split())
	if ch==3:
		cmd="virsh version"
		s_call(cmd.split())	
	if ch==4:
		cmd="virsh nodememstats"
		s_call(cmd.split())
	if ch==5:
		cmd="virsh -c qemu:///system list"
		s_call(cmd.split())
	if ch==6:
		cmd="virsh net-info default"
		s_call(cmd.split())
	if ch==7:
		cmd="virsh --connect qemu:///system"
		s_call(cmd.split())
	if ch==8:
		osname=raw_input("enter os name\n")
		cmd="virsh shutdown %s"%osname
		s_call(cmd.split())
	if ch==9:
		osname=raw_input("enter os name\n")
		cmd="virsh start %s"%osname
		s_call(cmd.split())
	if ch==10:
		osname=raw_input("enter os name\n")
		cmd="virsh suspend %s"%osname
		s_call(cmd.split())
	if ch==11:
		osname=raw_input("enter os name\n")
		cmd="virsh resume %s"%osname
		s_call(cmd.split())
	if ch==12:
		osname=raw_input("enter os name\n")
		cmd="virsh dominfo %s"%osname
		s_call(cmd.split())
	if ch==13:
		osname=raw_input("enter os name\n")
		cmd="virsh destroy %s"%osname
		s_call(cmd.split())
	if ch==14:
		osname=raw_input("enter os name\n")
		cmd="virsh define /etc/libvirt/qemu/%s.xml"%osname
		s_call(cmd.split())
		
	if ch==15:
		sys.exit()
		
