import os
from datetime import datetime
import time
from email import utils

def makeRFC2822Format(dateTimeObject):
    dateTuple = dateTimeObject.timetuple()
    dateTimeStamp = time.mktime(dateTuple)
    return utils.formatdate(dateTimeStamp, localtime=True)


if __name__ == '__main__':
    dateObj1 = datetime.strptime('Jun 1 2019  1:33PM', '%b %d %Y %I:%M%p')
    commitDate = makeRFC2822Format(dateObj1)
