from Program import progress_comand as pg
# klasa do generacji raportu


class PrepareReport(pg.ProgressCommand):
    def __init__(self, times1th, times4th, times4proc, timesxproc):
        self.__times1th = times1th
        self.__times4th = times4th
        self.__times4proc = times4proc
        self.__timesxproc = timesxproc
        self.__html_result = " "

    def execute(self):
        i = 0
        median1th = 0.0
        median4th = 0.0
        median4proc = 0.0
        medianxproc = 0.0
        self.__html_result = self.get_basic()
        self.__html_result = str(self.__html_result) + str(self.format_result_table(self.__times1th,
                                                                                    self.__times4th, self.__times4proc,
                                                                                    self.__timesxproc))
        for i in range(len(self.__times1th)):
            try:
                median1th = median1th + self.__times1th[i]
                median4th = median4th + self.__times4th[i]
                median4proc = median4proc + self.__times4proc[i]
                medianxproc = medianxproc + self.__timesxproc[i]
                if i == (len(self.__times1th) - 1):
                    # lista zaczyna sie od zara wiec do mediany potrzeba +1
                    i = i + 1
            except IndexError:
                print("Lack of results data")
            except TypeError:
                print("Wrong of results data")
        if i > 0:
            median1th = round((median1th/i), 3)
            median4th = round((median4th/i), 3)
            median4proc = round((median4proc/i), 3)
            medianxproc = round((medianxproc/i), 3)

        self.__html_result = str(self.__html_result) + str(self.format_median_table(median1th, median4th,
                                                                                    median4proc, medianxproc))
        self.__html_result = self.__html_result + str(self.format_footer())

    def get_result(self):
        return self.__html_result

    def get_basic(self):
        import platform
        import sys
        import os
        version = platform.python_version()
        interpret = platform.python_implementation()
        interpret_ver = sys.version
        operating_sys = platform.system()
        operating_sys_ver = platform.release()
        processor = platform.processor()
        cpu_count = os.cpu_count()
        return self.format_head(version, interpret, interpret_ver, operating_sys, operating_sys_ver, processor,
                                cpu_count)

    @staticmethod
    def format_head(version, interpret, interpret_ver, operating_sys, operating_sys_ver, processor, cpu_count):
        return str("<!DOCTYPE html>" +
                   "<html>" +
                   "<head>" +
                   "<title>Multithreading/Multiprocessing benchmark results</title>" +
                   "</head>" +
                   "<body>" +
                   "<h2>Multithreading/Multiprocessing benchmark results</h2>" +
                   "<h3>Execution enviroment</h3>" + "<p>Python version: " + str(version) +
                   "<br/>Interpreter: " + str(interpret) +
                   "<br/>Interpreter version: " + str(interpret_ver) +
                   "<br/>Operating system: " + str(operating_sys) +
                   "<br/>Operating system version: " + str(operating_sys_ver) +
                   "<br/>Processor: " + str(processor) +
                   "<br/>CPUs: " + str(cpu_count) + "</p>")

    @staticmethod
    def format_result_table(times1th, times4th, times4proc, timesxproc):
        ear: str = '"'
        er = 0
        intable = ""
        res1th, res4th, res4p, resxp = " ", " ", " ", " "
        for i in range(len(times1th)):
            try:
                res1th = str(times1th[i])
                res4th = str(times4th[i])
                res4p = str(times4proc[i])
                resxp = str(timesxproc[i])
            except IndexError:
                print("Lack of results data")
                er = 1
            except TypeError:
                print("Wrong of results data")
                er = 1

            if er == 0:
                intable = intable + str("<tr style=" + ear + "height: 18px;" + ear + ">" +
                                        "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >"
                                        + str(i + 1) + "</td>" +
                                        "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >"
                                        + res1th + "</td>" +
                                        "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >"
                                        + res4th + "</td>" +
                                        "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >"
                                        + res4p + "</td>" +
                                        "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >"
                                        + resxp + "</td></tr>")

        return str("<h3>Test results</h3>" +
                   "<p>The following table shows detailed test results:</p>" +
                   "<table style=" + ear + "border-collapse: collapse; width: 100%; height: 108px;" + ear + " border=" +
                   ear + "1" + ear + ">" +
                   "<tbody>" +
                   "<tr style=" + ear + "height: 18px;" + ear + ">" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>Execution</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>1 thread (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>4 threads (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>4 processes (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>Processes based on CPUs (s)</strong></td>" +
                   "</tr>" +
                   intable +
                   "</tbody></table>")

    @staticmethod
    def format_median_table(medianth, median4th, median4proc, medianxproc):
        ear = '"'
        return str("<h3>Summary</h3>" +
                   "<p>The following table shows median of all test results:</p>" +
                   "<table style=" + ear + "border-collapse: collapse; width: 100%; height: 108px;" + ear + " border=" +
                   ear + "1" + ear + ">" +
                   "<tbody>" +
                   "<tr style=" + ear + "height: 18px;" + ear + ">" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>Execution</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>1 thread (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>4 threads (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>4 processes (s)</strong></td>" +
                   "<td style=" + ear + "width: 20%; height: 18px; background-color: #aaaaaa;" +
                   ear + "><strong>Processes based on CPUs (s)</strong></td>" +
                   "</tr>" +
                   "<tr style=" + ear + "height: 18px;" + ear + ">" +
                   "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >Median </td>" +
                   "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >" + str(medianth) + "</td>" +
                   "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >" + str(median4th) + "</td>" +
                   "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >" + str(median4proc) + "</td>" +
                   "<td style = " + ear + "width: 20%; height: 18px;" + ear + " >" + str(medianxproc) + "</td>" +
                   "</tr>" +
                   "</tbody></table>")

    @staticmethod
    def format_footer():
        ear = '"'
        return str("<p style = " + ear + "text-align: right;" +
                   ear + "><strong>Author :</strong> <em>Arkadiusz Bratkowski</em></p>" +
                   "</body>")
