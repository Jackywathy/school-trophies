import sys
import datetime
import os
if __name__ == "__main__":
    print("Please import logger! dont run it dammit")
    sys.exit(100000000)


def LOG(string,default='log.txt'):
    with open(default) as out:
        print(datetime.datetime.now().strftime("[%y/%m/%d %H:%M:%S]"),'-',string,file=out)


def LOG_CLEAR(default='log.txt'):
    os.remove(default)

