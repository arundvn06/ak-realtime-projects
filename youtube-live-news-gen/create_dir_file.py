import errno
import os
from datetime import datetime

def pwd():
    return os.getcwd();

def crt_dir_with_today_date():
    mydir = os.path.join(os.getcwd(), datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(mydir)
        print("Directory created: ", mydir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    return mydir

def crt_dir_with_today_date_at_given_loc(dname):
    mydir = os.path.join(dname, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(mydir)
        print("Directory created: ", mydir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    return mydir    
    
def crt_file_with_today_date(fname):
    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    str_current_datetime = str(current_datetime)
    try:
        # create a file object along with extension
        file_name = os.getcwd() + "/" + str_current_datetime + fname
        file = open(file_name, 'w')
        print("File created : ", file.name)
        file.close()
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..   