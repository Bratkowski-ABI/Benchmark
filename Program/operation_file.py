import os
import time
# klasa r/w dla danychy i raportu


class FileOperation:
    def __init__(self, filename, reportname):
        self.__filename = filename
        self.__reportname = reportname
        self.__to_cnt = []

    def get_to_cnt(self):
        er = False
        backslash = "\\"
        path_file = os.getcwd() + backslash + "Data" + backslash + self.__filename
        if os.path.isfile(path_file):
            try:
                with open(path_file, "r") as data_file:
                    for line in data_file:
                        w = line.split(",")
                        for i in range(len(w)):
                            try:
                                self.__to_cnt.append(int(str(w[i])))
                            except OSError:
                                print("File not found, load default")
                                er = True
            except OSError:
                print("File not found, load default")
                er = True
        if er:
            self.__to_cnt = [15972490, 80247910, 92031257, 75940266, 97986012, 87599664, 75231321, 11138524,
                             68870499, 11872796, 79132533, 40649382, 63886074, 53146293, 36914087, 62770938]
        return self.__to_cnt

    def savereport(self, report):
        backslash = "\\"
        path_file = os.getcwd() + backslash + "Report" + backslash + self.__reportname
        while os.path.isfile(path_file):
            path_file = os.getcwd() + backslash + "Report" + backslash + str(time.time()) + self.__reportname
        try:
            f = open(path_file, "w")
            f.write(report)
            f.close()
        except OSError:
            return False
        return True
