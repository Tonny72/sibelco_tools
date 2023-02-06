import datetime
import glob
import sys


def find_latest_dts_in_raw_csv(path, tag, log):
    filename = find_latest_file_in_directory(path, tag, log)
    if filename == '':
        local_tz = datetime.datetime.now().astimezone().tzinfo
        dts = datetime.datetime(2000, 1, 1, 0, 0, 0)
        dts = dts.replace(tzinfo=local_tz)
        return dts
    else:
        try:
            with open(filename, "r") as f1:
                last_line = f1.readlines()[-1]
                dts = last_line.split(";")[0]
                # add zero's for nanaseconds to get the correct format for parsing
                dts = dts + '000'
                dts = datetime.datetime.strptime(dts, '%Y-%m-%d %H:%M:%S.%f')
                local_tz = datetime.datetime.now().astimezone().tzinfo
                dts = dts.replace(tzinfo=local_tz)
            return dts
        except:  # catch *all* exceptions
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

        return datetime.datetime(2000, 1, 1, 0, 0, 0)


def find_latest_file_in_directory(path, tag, log):
    filePattern = path + "/*" + tag + "_" + log + ".csv"
    files = glob.glob(filePattern)
    files.sort()
    if (len(files)) > 0:
        latest_file = files[-1]
    else:
        latest_file = ''
    return latest_file