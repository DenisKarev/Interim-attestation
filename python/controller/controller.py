from views.commandline import commandline
from dbase.gnotesdb import gnotes_db
from views.commandinput import commandinput
# from dbase.gnote import gnote
from models.gview import gview
from sys import exit, argv


class controller():
    v: commandline
    db: gnotes_db
    inp: commandinput

    last: int

    def __init__(self, v, db) -> None:
        self.v = v
        self.db = db
        self.inp = commandinput()
        self.last = 0

    def run(self):
        if len(argv)==1:
            self.inp.parser.print_help()
            exit(0)
        self.inp.get_args()     # Parse arguments to inp.args_dict: dict
        if self.db.get_status():
            self.db.read_db()
            # self.db.rebuild_indexes()
            self.last = self.db.get_index()

        # sort option
        # if self.inp.args_dict['o'] != None:
        #     self.v.sort = self.inp.args_dict['o']
        #     print('Sort option!')

        if self.inp.args_dict['l'] != False:
            self.list_notes()

        elif self.inp.args_dict['a'] != None:
            self.add_note()

        elif self.inp.args_dict['e'] != None:
            self.edit_note()

        elif self.inp.args_dict['d'] != None:
            self.delete_note()

        elif self.inp.args_dict['s'] != None:
            self.show_note()

    def add_note(self):
        a0=self.inp.args_dict['a'][0]
        a1=self.inp.args_dict['a'][1]
        # print(f'a= {a0}, {a1}')
        # gn = gnote(self.last, a0, a1)
        idx = self.db.add_gnote(self.last+1, a0, a1)
        self.v.gnote_print('Added note:\t', self.db.get_gnote(idx), t='s')
        self.last += 1
        exit(0)

    def list_notes(self):
        if self.last <= 0:
            self.v.err_print('Do not have any notes. gntsc -h for help )')
        else:
            for n in self.db.gnotes:
                self.v.gnote_print('', n, 's')
        exit(0)

    def edit_note(self):
        if self.last <= 0:
            self.v.err_print('Do not have any notes. gntsc -h for help )')
            exit(0)

        idx = self.inp.args_dict['e'][0]

        # print(idx, self.db.get_index()-1, self.inp.args_dict['t'][0], self.inp.args_dict['b'][0])
        # print(type(idx), type(self.db.get_index()-1), type(self.inp.args_dict['t'][0]), type(self.inp.args_dict['b'][0]))
        
        if idx >= 0 and idx <= self.db.get_index()-1:    # if index in working range
            if self.inp.args_dict['t'][0] == None or self.inp.args_dict['b'][0] == None:
                self.v.edit_usage()
            else:
                if self.inp.args_dict['t'][0] != None:
                    self.db.gnotes[idx]['title'] = self.inp.args_dict['t'][0]
                if self.inp.args_dict['b'][0] != None:
                    self.db.gnotes[idx]['notetext'] = self.inp.args_dict['b'][0]
                self.db.write_db()
                self.v.gnote_print('Edited note:\t', self.db.get_gnote(idx+1), t='s')
        exit(0)

    def delete_note(self):
        if self.last <= 0:
            self.v.err_print('Do not have any notes. gntsc -h for help )')
        else:
            idx = self.inp.args_dict['d'][0]
            if idx >= 0 and idx <= self.db.get_index():    # if index in working range
                print(self.db.get_index())
                old = self.db.del_gnote(idx)
                print(self.db.get_index())
                self.v.gnote_print('Deleted note:\t', old, t='s')
                self.db.write_db()
            else:
                self.v.err_print(f'Note index out of range: {idx}')
        exit(0)

    def show_note(self):
        if self.last <= 0:
            self.v.err_print('Do not have any notes. gntsc -h for help )')
        else: 
            idx = self.inp.args_dict['s'][0]
            if idx >= 0 and idx <= self.db.get_index():    # if index in working range
                self.v.gnote_print('Edited note:\t', self.db.get_gnote(idx-1), t='f')
            else:
                self.v.err_print(f'Note index out of range: {idx}')
            exit(0)


#region
        # for o, a in self.inp.opts:
        #     if o == "-?":
        #         self.v.status(self.db.get_status())
        #         exit(0)
        #     elif o in ("-a"):
        #         print(a.split())
        #         print(f'{self.last}, {a}, {0}', a.split())
        #         # self.db.add_gnote(gnote(self.last, a[0], a[1]))
        #         # self.db.write_db()
        #         exit(0)
        #     elif o in ("-d"):
        #         try:
        #             self.db.del_gnote(self.inp.args)
        #         except:
        #             pass
        #     elif o in ("-e"):
        #         try:
        #             gn = int(self.inp.args)
        #         except:
        #             self.v.wrong_int()
        #             exit(2)
        #         try:
        #             self.db.mod_gnote(gn)
        #         except:
        #             pass

        #     elif o in ("-s"):
        #         try:
        #             self.db.get_gnote(self.inp.args)
        #         except:
        #             pass
        #     elif o in ("-h"):
        #         print(type(self.v))
        #         self.v.usage()
        #         exit(0)
        #     else:
        #         self.v.shorthelp()
        #         return (-1)
#endregion