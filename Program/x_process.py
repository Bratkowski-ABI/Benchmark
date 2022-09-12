import main
from Program import progress_comand as pg
# klasa procesow


class XProcess(pg.ProgressCommand):
    def __init__(self, to_cnt_list, proc_cnt):
        self.to_cnt_list = to_cnt_list
        self.proc_cnt = proc_cnt

    def execute(self):
        from multiprocessing import Pool

        if self.proc_cnt > 0:
            with Pool(self.proc_cnt) as p:
                p.map(main.calculate, self.to_cnt_list)
        else:
            print("wrong process size")
