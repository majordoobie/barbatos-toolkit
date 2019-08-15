import os, sys, hashlib

def get_hash(hashfile):
	md5sum = hashlib.md5()
	sha1sum = hashlib.sha1()
	sha256sum = hashlib.sha256()
	while True:
		bin = hashfile.read(65536)
		if not bin:
			break
		md5sum.update(bin)
		sha1sum.update(bin)
		sha256sum.update(bin)
	return(md5sum.hexdigest(),sha1sum.hexdigest(),sha256sum.hexdigest())
	
def help():
	print("\n ------> win_hash.py [option] file.")
	print("\nOPtions:
	print("    --md5sum")
	print("    --sha1sum")
	print("    --sha256sum")
	print("    --help")
	print("No options = ALL hashes")
	
if __name__=='__main__':
	if len(sys.argv) == 1 or sys.argv[1] in ["--help","-h","/?"]:
		help()
	if len(sys.argv) == 2:
		if os.path.isfile(sys.argv[1]):
			with open(sys.argv[1], 'rb') as hashfile:
				md5,sha1,sha256 = get_hash(hashfile)
			print("File: {}\nmd5sum: {}".format(os.path.abspath(sys.argv[1]),md5))
			print("sha1sum: {}".format(sha1))
			print("sha256sum: {}".format(sha256))
		else:
			sys.exit("File supplied does not exist")
	elif len(sys.argv) == 3:
		if os.path.isfile(sys.argv[1]):
			if sys.argv[2] in ["--md5sum","--sha1sum","--sha256sum"]:
				with open(sys.argv[1],'rb') as hashfile:
					md5,sha1,sha256 = get_hash(hashfile)
				if sys.argv[2] == '--md5sum':
					print("File: {}\nmd5sum: {}".format(os.path.abspath(sys.argv[2]),md5))
				elif sys.argv[2] == '--sha1sum':
					print("File: {}\nsha1sum: {}".format(os.path.abspath(sys.argv[2]),sha1))
				elif sys.argv[2] == '--sha256sum':
					print("File: {}\nsha256sum: {}".format(os.path.abspath(sys.argv[2]),sha256))
				else:
					sys.exit()
			else: 
				sys.exit("Arguments not supported, check win_hash.py --help")
		elif os.path.isfile(sys.argv[2]):
			if sys.argv[1] in ["--md5sum","--sha1sum","--sha256sum"]:
				with open(sys.argv[2],'rb') as hashfile:
					md5,sha1,sha256 = get_hash(hashfile)
				if sys.argv[1] == '--md5sum':
					print("File: {}\nmd5sum: {}".format(os.path.abspath(sys.argv[2]),md5))
				elif sys.argv[1] == '--sha1sum':
					print("File: {}\nsha1sum: {}".format(os.path.abspath(sys.argv[2]),sha1))
				elif sys.argv[1] == '--sha256sum':
					print("File: {}\nsha256sum: {}".format(os.path.abspath(sys.argv[2]),sha256))
				else:
					sys.exit()
			else: 
				sys.exit("Arguments not supported, check win_hash.py --help")
		else:
			sys.exit("File supplied does not exist.")
