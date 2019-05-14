import os, sys
from math import floor
from random import randint

"""
    Global variables
"""
delimiterBoolean = False
outputBoolean = False
Gobal = delimiterBoolean
Global = outputBoolean


def help():
    helpp = """
python numGen.py [-l length] [-n iteration] [-d delimiter:sequence] [-o output file]
Description: The tool is used to generate a random length of numbers with the option
             to supply a delimiter for the purpose of brute forcing recovery keys.
    -l  [MANDATORY] The length of the number to be generated.
    -n  [MANDATORY] How many times to generate a random number. Each number generated
        will be appended to a text file with a new line.
    -d  [OPTIONAL] A delimter character followed by a sequence number used to inject
        the delimiter into the chain of numbers generated.
    -o [OPTIONAL] Output text file. By default, a randomly named file will be created
        in the working directory of the script.
Examples:
    input:
     python numGen.py -l 6 -n 3
    output:
     513846
     481263
     845134
    input:
     python numGen.py -l 48 -n 2 -d -:6
    output:
     158456-215478-965123-548562-974197-468546-184581-658843
     481185-846843-138437-816399-666345-448713-846894-618480
    input:
     python numGen.py -l 8 -n 1 -d @:2 -o C:\output.txt
    output:
     69@04@48@99
    
    """
    sys.exit(helpp)

def applyDelimiter(num, delimiter, sequence):
    numList = [ i for i in str(num) ]
    if numList.__len__() % sequence == 0:
        slices = int(numList.__len__() / sequence) -1
    else:
        slices = floor(numList.__len__() / sequence)
    
    slicer = int(sequence)
    for i in range(slices):
        numList.insert(slicer, delimiter)
        slicer += int(sequence) + 1
    string = ""
    for i in numList:
        string +=str (i)
    return string

def defaultGenerator(length, iteration):
    print("Creating file...")
    fileName = "numGen" + str(randint(10000, 999999)) + ".txt"
    with open(fileName, "w", encoding = "utf-8") as outfile:
        for i in range(iteration):
            outfile.write(str(randint((10**(length-1)), ((10**length)-1))))
            outfile.write("\n")
    print("Done.")


def delimiterGenerator(length, iteration, delimiter, sequence):
    print("Creating file...")
    fileName = "numGen" + str(randint(10000, 999999)) + ".txt"
    with open(fileName, "w", encoding = "utf-8") as outfile:
        for i in range(iteration):
            num = str(randint((10**(length-1)), ((10**length)-1)))
            outfile.write(applyDelimiter(num, delimiter, sequence))
            outfile.write("\n")
    print("Done.")

if __name__ == "__main__":
    helper = ["/?", "-h", "--help"]
    for i in sys.argv:
        if i in helper:
            help()
    if "-l" and "-n" not in sys.argv:
        sys.exit("You must provide the -l and -n switches. Please use the -h for help.")
    else:
        try:
            sys.argv[sys.argv.index("-l") + 1 ]
            if str(sys.argv[sys.argv.index("-l") + 1 ]).isdigit() == False:
                sys.exit("-l must be accompanied by an integer. Please use -h for help.")
        except:
            sys.exit("-l switch must have a integer after it. Please use -h for help.")
        try:
            sys.argv[sys.argv.index("-n") + 1 ]
            if str(sys.argv[sys.argv.index("-n") + 1 ]).isdigit() == False:
                sys.exit("-n must be accompanied by an integer. Please use -h for help.")
        except:
            sys.exit("-n switch must have a integer after it. Please use -h for help.")
    
    length = sys.argv[sys.argv.index("-l") + 1]
    iteration = sys.argv[sys.argv.index("-n") + 1]

    if "-d" in sys.argv:
        try: 
            sys.argv[sys.argv.index("-d") + 1]
        except:
            sys.exit("The -d option must be followed by a delimiter character a colon and an integer.")

        if ":" in sys.argv[sys.argv.index("-d")+1]:
            delimiterList = sys.argv[sys.argv.index("-d") + 1].split(":")
            if delimiterList.__len__() == 2:
                if str(delimiterList[-1].isdigit()):
                    if int(delimiterList[-1]) < int(length):
                        delimiterBoolean = True
                        delimiter = delimiterList[0]
                        sequence = delimiterList[-1]
                    else:
                        sys.exit("The sequence provided exceeds the length of the number being generated.")
                else:
                    sys.exit("Delimiter sequence has to be an integer.")
            else:
                sys.exit("There was a problem when splitting your delimiter options.")
        else:
            sys.exit("Must provide a colon seperating the delimiter string and sequence number in which to inject to.")

    if delimiterBoolean == False and outputBoolean == False:
        defaultGenerator(int(length), int(iteration))
    if delimiterBoolean == True and outputBoolean == False:
        delimiterGenerator(int(length), int(iteration), delimiter, int(sequence))
