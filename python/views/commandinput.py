from sys import argv, exit
from getopt import getopt, GetoptError, gnu_getopt
# import getopt, sys
from argparse import ArgumentParser


class commandinput():
    parser: ArgumentParser
    parce_dict: dict

    # args: str
    # opts: str

    # def __init__(self) -> None:
    #     print(argv[1:]) # TODO #
    #     try:
    #         self.opts, self.args = getopt(argv[1:], "a:d:e:s:hl?")
    #     except GetoptError as err:
    #         # print help information and exit:
    #         print(err)  # will print something like "option -a not recognized"
    #         exit(1)
    #     finally:
    #         print(type(self.opts))
    #         print(type(self.args))

    def __init__(self) -> None:
        self.parser = ArgumentParser(prog='gNotes', description='',
                    epilog='Example: python[3] gtnts.py -a " Example title" "Example body of the note!"', add_help=True)
        self.parser.add_argument('-a', metavar='"text"', nargs=2, help='adds a note. First part is "Title" second is "Body of the note"')
        self.parser.add_argument('-e', nargs=1, metavar='int', type=int, help='edits a note by "int" use -t "text" or/and -b "text" options')
        self.parser.add_argument('-t', nargs=1, metavar='text', type=str, help='defines "Title" text of the note')
        self.parser.add_argument('-b', nargs=1, metavar='text', type=str, help='defines "Body" text of the note')

        self.parser.add_argument('-d', nargs=1, metavar='int', type=int, help='deletes a note by "int"')
        self.parser.add_argument('-s', nargs=1, metavar='int', type=int, help='shows a note by "int"')
        self.parser.add_argument('-l', action='store_true', help='lists notes')
#        self.parser.add_argument('-o', nargs=1, metavar='(a/r)', choices=['a', 'd'], help='Option sort (a/r) (Acsending/Descending)')
        self.parce_dict = vars(self.parser.parse_args())


if __name__ == '__main__':
    ci = commandinput()
    args = ci.parser.parse_args()
    print(args.a, args.b, args.t)
    print(ci.parce_dict)
    print(type(ci.parce_dict['e'][0]))
    print(ci.parce_dict['e'][0])