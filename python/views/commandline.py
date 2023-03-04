from models.gview import gview
from datetime import datetime

class commandline():
    sortoption: str     # if implenemt sor option ))
    edit_usage: str

    def __init__(self) -> None:
        self.sortoption = ''
        self.edit_usage = '-e usage string'
        # self.empty = f'Nothing to {} -- base is empty'

    def edit_usage(self):
        print(self.edit_usage)
        print(self.help_txt)

    def err_print(self, text):
        print(text)


    def gnote_short_print(self, n: dict):
        idx = n['index']
        tit = n['title']
        cmdate = datetime.fromtimestamp(n['cmdate']).strftime("%d/%m/%Y %H:%M:%S")
        return f'{idx}\t{tit}\t{cmdate}'
    
    def gnote_full(self, n: dict) -> str:
        idx = n['index']
        tit = n['title']
        text = n['notetext']
        cmdate = datetime.fromtimestamp(n['cmdate']).strftime("%d/%m/%Y %H:%M:%S")
        return f'{idx}\t{tit}\t{text}\t{cmdate}'

    def gnote_print(self, message: str, gn: dict, t: str):
        if t in 'sf':
            if t == 'f': print(f'{message} {self.gnote_full(gn)}')
            else:  print(f'{message} {self.gnote_short_print(gn)}')
