import time
from Program import x_thread as xth
from Program import x_process as xproc
from Program import prepare_report as pr
from Program import operation_file as op


def progress(commands):
    times = []
    for i, cmd in enumerate(commands, start=1):
        signs = int(i / len(commands) * 10)
        done = '#' * signs
        to_do = ' ' * (10 - signs)
        print("|" + done + to_do + "|\r", end='')
        timest = time.time()
        cmd.execute()
        timeed = time.time()
        times.append(round((timeed - timest), 3))
    print()
    time.sleep(1)
    return times


def calculate(number):
    result = 0
    try:
        for i in range(1, number):
            result = result + ((number - i) * i)
    except TypeError:
        print("Calculation require numeric")
    return result


def cnt_cpu():
    import os
    return os.cpu_count()


def main():
    time_begin = time.time()
    file_name = "numbers.csv"
    reportname = "report.html"
    print("Multithreading/Multiprocessing benchmark")
    print("Step 1/7")
    cpu_count = cnt_cpu()
    fileoper = op.FileOperation(file_name, reportname)
    to_count = fileoper.get_to_cnt()
#    to_count = [1, 80, 12, 75, 9, 874, 21, 14,
#                             49, 1, 73, 4, 74, 53, 7, 68]
    print("Step 2/7")
    cnt_one_th_1 = xth.XThread(to_count, 1)
    cnt_one_th_2 = xth.XThread(to_count, 1)
    cnt_one_th_3 = xth.XThread(to_count, 1)
    cnt_one_th_4 = xth.XThread(to_count, 1)
    cnt_one_th_5 = xth.XThread(to_count, 1)
    time_of_one_th = progress([cnt_one_th_1, cnt_one_th_2, cnt_one_th_3, cnt_one_th_4, cnt_one_th_5])
    print("Step 3/7")
    cnt_four_th_1 = xth.XThread(to_count, 4)
    cnt_four_th_2 = xth.XThread(to_count, 4)
    cnt_four_th_3 = xth.XThread(to_count, 4)
    cnt_four_th_4 = xth.XThread(to_count, 4)
    cnt_four_th_5 = xth.XThread(to_count, 4)
    time_of_four_th = progress([cnt_four_th_1, cnt_four_th_2, cnt_four_th_3, cnt_four_th_4, cnt_four_th_5])
    print("Step 4/7")
    cnt_four_proc_1 = xproc.XProcess(to_count, 4)
    cnt_four_proc_2 = xproc.XProcess(to_count, 4)
    cnt_four_proc_3 = xproc.XProcess(to_count, 4)
    cnt_four_proc_4 = xproc.XProcess(to_count, 4)
    cnt_four_proc_5 = xproc.XProcess(to_count, 4)
    time_of_four_proc = progress([cnt_four_proc_1, cnt_four_proc_2, cnt_four_proc_3, cnt_four_proc_4, cnt_four_proc_5])
    print("Step 5/7")
    cnt_x_proc_1 = xproc.XProcess(to_count, cpu_count)
    cnt_x_proc_2 = xproc.XProcess(to_count, cpu_count)
    cnt_x_proc_3 = xproc.XProcess(to_count, cpu_count)
    cnt_x_proc_4 = xproc.XProcess(to_count, cpu_count)
    cnt_x_proc_5 = xproc.XProcess(to_count, cpu_count)
    time_of_x_proc = progress([cnt_x_proc_1, cnt_x_proc_2, cnt_x_proc_3, cnt_x_proc_4, cnt_x_proc_5])
    print("Step 6/7")
    report = pr.PrepareReport(time_of_one_th, time_of_four_th, time_of_four_proc, time_of_x_proc)
    report.execute()
    print("Step 7/7")
    if fileoper.savereport(report.get_result()):
        print(" -> Report save")
    else:
        print(" -> Error with saving report")
    time_end = time.time()
    print("Benchmark end in ", (time_end - time_begin), " sec")


if __name__ == '__main__':
    main()
