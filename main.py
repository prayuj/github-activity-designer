import os
from datetime import datetime
import time
from email import utils
FILE__PATH = "./temp/commit.txt"

def makeRFC2822Format(dateTimeObject):
    dateTuple = dateTimeObject.timetuple()
    dateTimeStamp = time.mktime(dateTuple)
    return utils.formatdate(dateTimeStamp, localtime=True)

def addFile():
    with open(FILE__PATH, 'w') as fp:
        fp.write("Creating this file")


def deleteFile():
    os.remove(FILE__PATH)

if __name__ == '__main__':
    dateObj1 = datetime.strptime('Jun 1 2019  1:33PM', '%b %d %Y %I:%M%p')
    commitDate = makeRFC2822Format(dateObj1)
    if os.path.isfile(FILE__PATH):
        deleteFile()
    else:
        addFile()

    os.system('git add .')
    os.system('git commit --date="%s" --no-edit -m "Fake Commit"' % (commitDate))
