from dbase.fileio import fileio
# from dbase.gnote import gnote
from datetime import datetime


class gnotes_db():
    gnotes: list
    fio: fileio
    gnotefile: str

    def __init__(self, filename) -> None:
        """ gnotes database
        filename = file to store data"""
        self.fio = fileio(filename)
        self.index = 0
        self.gnotes = []
        self.gnotefile = filename

    def add_gnote(self, idx, tit, text) -> int:
        nn = {}
        nn['title'] = tit
        nn['index'] = idx
        nn['notetext'] = text
        nn['cmdate'] = datetime.now().timestamp()
        self.gnotes.append(nn)
        self.fio.write_json_file(self)
        return self.get_index()-1

    def get_gnote(self, i: int) -> dict:
        return self.gnotes[i]

    def del_gnote(self, i: int) -> None:
        return self.gnotes.pop(i-1)
        # self.fio.write_db(self.gnotes)

    def mod_gnote(self, i: int, gn: dict) -> None:
        pass

    def get_index(self) -> int:
        if len(self.gnotes) == 0:
            return len(self.gnotes)
        else:
            return self.get_gnote(len(self.gnotes)-1)['index']

    def rebuild_indexes(self):
        self.index = 1
        for n in self.gnotes:
            n['index'] = self.index
            self.index += 1

    def get_status(self) -> bool:
        return self.fio.file_status()

    def read_db(self) -> None:
        if self.get_status():
            self.fio.read_json_file(self)
        self.index = len(self.gnotes)

    def write_db(self) -> None:
        self.fio.write_json_file(self)


if __name__ == "__main__":
    from gnote import gnote
    from fileio import fileio
    gdb = gnotes_db()
    print(gdb.get_status())
