import json
from os.path import isfile
from os import remove, stat

# if False:
# from dbase.gnotesdb import gnotes_db

class fileio():
    gnotefile: str

    def __init__(self, filename) -> None:
        self.gnotefile = filename

    def file_status(self) -> bool:
        if isfile(self.gnotefile):
            if stat(self.gnotefile).st_size < 1:
                # print('removed')
                remove(self.gnotefile)
                return False
            else: return True
        return False

    def read_json_file(self, db: 'gnotes_db') -> None:
        with open(self.gnotefile, 'r', encoding='UTF-8') as gfr:
            # try:
                db.gnotes = json.load(gfr)
            # except json.JSONDecodeError:
            #     pass

    def write_json_file(self, db: 'gnotes_db') -> None:
        with open(self.gnotefile, 'w', encoding='UTF-8') as gfw:
            json.dump(db.gnotes, gfw, indent=7, default=vars)
