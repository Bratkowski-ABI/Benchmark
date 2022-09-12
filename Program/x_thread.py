import main
from Program import progress_comand as pg
# klasa watku


class XThread(pg.ProgressCommand):
    def __init__(self, to_cnt_list, th_cnt):
        self.__to_cnt_list = to_cnt_list
        self.__th_cnt = th_cnt

    def execute(self):
        import threading
        threadlist = list()
        if self.__th_cnt == 1:
            t = threading.Thread(target=self.calculate, args=(self.__to_cnt_list,))
            t.start()
            t.join()
        elif self.__th_cnt > 1:
            mid_elements = []
            mid_elements_list = []
            try:
                calculate_elements = len(self.__to_cnt_list) / self.__th_cnt
                if calculate_elements < 1:
                    # nie da sie zapelnic wszystkich list jednym elementem
                    # dzialanie jednowatkowe, wszystkie ementy na pierwszej liscie
                    empty = []
                    mid_elements = self.__to_cnt_list
                    mid_elements_list.append(mid_elements)
                    for i in range(1, self.__th_cnt):
                        mid_elements_list.append(empty)
                else:
                    calculate_elements = int(calculate_elements)
                    for i in range(self.__th_cnt - 1):
                        if i == self.__th_cnt - 1:
                            for y in range((i * calculate_elements + i), len(self.__to_cnt_list)):
                                mid_elements.append(self.__to_cnt_list[y])
                        else:
                            # ostatnia lista dopelniona o elementy "reszty z dzielenia
                            for y in range((i * calculate_elements + i), ((i + 1) * calculate_elements)):
                                mid_elements.append(self.__to_cnt_list[y])
                        mid_elements_list.append(mid_elements)
                        mid_elements = []
                for i in range(self.__th_cnt - 1):
                    t = threading.Thread(target=self.calculate, args=(mid_elements_list[i],))
                    t.start()
                    threadlist.append(t)
                for th in threadlist:
                    th.join()
            except TypeError:
                print("Wrong element calculation")
            except IndexError:
                print("Wrong index calculation")
        else:
            print("wrong thread size")

    @staticmethod
    def calculate(cntlist):
        # wewnetrzna funkcja watka dzieli elementy na liste i uruchamia funkcje liczenia z main
        try:
            for i in range(len(cntlist)):
                main.calculate(cntlist[i])
        except IndexError:
            print("Not a list to calculate")
