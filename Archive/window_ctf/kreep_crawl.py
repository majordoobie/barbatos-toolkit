import os, sys, math, datetime, glob
from pathlib import Path
from operator import itemgetter

def helper():
    string = """
    python lister.py <file path>

    For recursive use -r or --recursive
        python lister.py -r <file path>
    """
    print(string)
    sys.exit()

def convert_size(size):
    if size == 0:
        return "0B"
    size_name = ("B","KB","MB","GB","TB") 
    #Calculate the exponent required to
    #get 1024 to size then round down to use as index 
    index = int(math.floor(math.log(size, 1024))) 

    # raise the 1024 size to the power that reflects the 
    # tier of size we're dealing with
    tier = math.pow(1024, index)

    #divid the bytes by the tier to get a three digit number with a 2 precision
    human_size = round(size / tier , 2)
    return "{} {}".format(human_size, size_name[index])

def add_dir_sizes(filer):
    return os.stat(filer).st_size

def listIt(directory):
    for item in os.listdir(directory):
        if os.path.isfile(directory / item):
            meta = os.stat(directory / item)
            mtime = datetime.datetime.fromtimestamp(meta.st_mtime).strftime("%d%b%Y %H:%M").upper()
            print("f > {} {:>10} {}".format(mtime,convert_size(meta.st_size),os.path.abspath(directory / item)))
        else:
            zero = "0 B"
            meta = os.stat(directory / item)
            mtime = datetime.datetime.fromtimestamp(meta.st_mtime).strftime("%d%b%Y %H:%M").upper()
            print("d > {} {:>10} {}".format(mtime,zero,os.path.abspath(directory / item)))
        
def recursiveDir(directory):
    for item in os.listdir(directory):
        if os.path.isfile(directory / item):
            meta = os.stat(directory / item)
            mtime = datetime.datetime.fromtimestamp(meta.st_mtime).strftime("%d%b%Y %H:%M").upper()
            print("f > {} {:>10} {}".format(mtime,convert_size(meta.st_size),os.path.abspath(directory / item)))
        else:
            listIt(directory / item)

"""
    recursiveSize will get the sizes of each directory that you're looking at
"""
def recursiveSize(directory):
    master_list_file = []
    master_list_dir = []
    for item in os.listdir(directory):
        if Path(directory / item).is_file():
            meta = os.stat(directory / item)
            mtime = datetime.datetime.fromtimestamp(meta.st_mtime).strftime("%d%b%Y %H:%M").upper()
            master_list_file.append(["f > {} {:>10} {}".format(mtime,convert_size(meta.st_size),os.path.abspath(directory / item)), meta.st_size])
            
        elif Path(directory / item).is_dir():
            tote = 0
            print("Working on: /ls -=l{}".format(item))
            for r_file in Path(directory / item).glob('**'):
                if Path(r_file).is_file():
                    tote += Path(r_file).stat().st_size
            meta = Path(directory / item).stat()
            mtime = datetime.datetime.fromtimestamp(meta.st_mtime).strftime("%d%b%Y %H:%M").upper()
            master_list_dir.append(["d > {} {:>10} {}".format(mtime,convert_size(tote),os.path.abspath(directory / item)), tote])
    
    #Sort our lists by file sizes
    for i in sorted(master_list_file, key=itemgetter(1)):
        print(i[0])
    print("")
    for i in sorted(master_list_dir, key=itemgetter(1)):
        print(i[0])



if __name__ == "__main__":
    start = datetime.datetime.now()
    helpList = ["-h","--help","/?"]
    if any( x in helpList for x in sys.argv):
        helper()

    #without arguments, it'll list current dir
    elif len(sys.argv) == 2:
        dirpath = Path(sys.argv[-1])
        print(dirpath)
        listIt(dirpath)

    # recurse will give you all the sub levels in the current 
    # dir that you supplied 
    elif len(sys.argv) > 2:
        if "-r" in sys.argv or "--recursive" in sys.argv:
            if "-r" in sys.argv:
                index = sys.argv.index("-r")
            else:
                index = sys.argv.index("--recursive")
            if index == 1:
                dirpath = Path(sys.argv[2])
            else:
                dirpath = Path(sys.argv[1])
            recursiveDir(dirpath)

        # all size is the bread and butter of this scritp. 
        # not only will it recurse but it should return the 
        # total size of a directory 
        elif "--allsize" in sys.argv:
            if "-f" not in sys.argv:
                sys.exit("Need to provide a -f for this option")   
            else:
                index = sys.argv.index("-f")
                try:
                    test = sys.argv[index+1]
                except:
                    sys.exit("Make sure that the file path is followed by the -f option.")

                if sys.argv[index+1] != "--allsize":
                    dirpath = Path(sys.argv[index+1])
                else:
                    sys.exit("Make sure that the file path is follwed by the -f.")

            recursiveSize(dirpath)

        else:
            sys.exit("Wrong arguments used.")
    else:
        helper()
    end = datetime.datetime.now()
    print("\n\nProgram took: {} seconds.".format((end-start).seconds))
