from datetime import datetime  # ,date, time


class gnote():
    index: int
    title: str
    notetext: str
    cmdate: float

    def __init__(self, idx: int, tit: str, ntext: str) -> None:
        self.index = idx
        self.title = tit
        self.notetext = ntext
        self.cmdate = datetime.now().timestamp()

    def short(self) -> str:
        return f'{self.index}\t {self.title}\t\
        {datetime.fromtimestamp(self.cmdate).strftime("%d/%m/%Y %H:%M:%S")}'

    # def __str__(self) -> str:
    #     return f'{self.index}\t {self.title}\t\t {self.notetext}\t\
    #     {datetime.fromtimestamp(self.cmdate).strftime("%d/%m/%Y %H:%M:%S")}'

if __name__ == "__main__":
    # datetime object containing current date and time
    now = datetime.now()
    print("now =", now)
    print("stamp", now.timestamp())


    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    # dt_from_tstamp = datetime.fromtimestamp(now)
    # print(dt_from_tstamp)
