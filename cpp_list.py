import sys

fp = open("/home/min/tmp/git_info/cpp_list", "r")
for line in fp.readlines():
#	line.strip()
#	print "hello %s" % line
	sys.stdout.write("%s" % line)
fp.close()

#line = "hello1\n"
#print "%s" % line
