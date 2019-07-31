#!/usr/bin/python3
from sys import argv
from datetime import datetime, timedelta

def help():
    msg = ("\nSimple script used to create multiple wevtutil pastables. It is expected "
    "that you run\n\n "
    "** dir c:\\Windows\\System32\\winevt\\Logs /o:d /t:w /a:-d **\n\n"
    "to see what logs could have updated when you logged in using the "
    "wmic os get localdatetime as a comparison. "
    "\nOnce you have identified the logs you need to look into, run the dir command "
    "again but this time with a /b \n\n "
    "** dir c:\\Windows\\System32\\winevt\\Logs /o:d /t:w /a:-d /b **\n\n"
    "then copy and paste the output into this script. "
    "You will then be  prompted to input your\n\n "
    "** wmic os get localdatetime **\n\n"
    "output, make sure that it was ran when you initially logged on or else it defeats the purpose. "
    "By dafault the program will substract 10 mintues to your time input as a safety buffer.")

    exit(msg)

def parse_input():
    """ Parse out the input using Input() """
    print("\n\ndir c:\\Windows\\System32\\winevt\\Logs /o:d /t:w /a:-d /b\n\n")
    all_logs = []
    print("Paste the log titles then press enter:\n")
    while True:
        raw = input("> ").strip()
        if len(raw) == 0:
            break
        else:
            print(raw)
            all_logs.append(raw)

    print("\n\nwmic os get localdatetime\n\n")
    current_time = input("Paste in your wmic os get localdatetime:\n> ")
    print("\n")
    current_time.split(".")[0]
    current_time = datetime.strptime(current_time.split(".")[0], "%Y%m%d%H%M%S")
    current_time = current_time - timedelta(minutes=10)

    main(all_logs, current_time)

def clean_logs(all_logs):
    """ When pasting the out from dir, winders adds a %4 that represents a / we
    need to convert it back to / and also remove the file extension of .evtx """

    for index,logname in enumerate(all_logs):
        all_logs[index] = (logname.replace("%4", "/")).split(".")[0]
    return all_logs


def main(all_logs, current_time):
    """ Takes in the input from parse_input and creates a easy to copy output """

    all_logs = clean_logs(all_logs)
    str_date = current_time.strftime("%Y-%m-%dT%H:%M:%S")
    date_query = "/q:*[System[TimeCreated[@SystemTime>'{}']]]".format(str_date)
    for log in all_logs:
        print("wevtutil qe \"{}\" \"{}\" /format:text".format(log, date_query))

if __name__ == '__main__':
    if len(argv) == 1:
        parse_input()
    else:
        help()
