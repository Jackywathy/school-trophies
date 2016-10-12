import os
from argparse import ArgumentTypeError, ArgumentParser, ArgumentDefaultsHelpFormatter
import csv
import collections
import trophy, plaque

K_NAME = "parser"

__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Beta 1.3'


class CsvFileParser:
    def __init__(self, fileobj, allcsv=False, delimiter=','):
        self.trophy_points = []
        self.plaque_points = []
        self.csv = []
        self.current = None
        for line in fileobj:
            proc = line.rstrip()
            if proc.replace(' ',''):
                if allcsv:
                    self.csv.append(proc)
                elif proc.startswith("{CSV}"):
                    self.current = self.csv
                elif proc.startswith("{TROPHY_LIMITER}"):
                    self.current = self.trophy_points
                elif proc.startswith("{PLAQUE_LIMITER}"):
                    self.current = self.plaque_points
                else:
                    try:
                        self.current.append(proc)
                    except AttributeError:
                        raise ValueError("Missing Declarations!")
        self.trophy_points = [self.check_size(tuple(map(int,i.split())), 9) for i in self.trophy_points]
        self.plaque_points = [self.check_size(tuple(map(int,i.split())), 153) for i in self.plaque_points]
        csv_obj = csv.reader(self.csv, delimiter=delimiter)
        self.TROPHY=[]
        self.PLAQUE=[]

        for item in csv_obj:
            print(item)
            if len(item) != 3:
                print(item, "IS not right length")
                continue
            if item[0].upper() == "SCHOOL_TROPHY":
                self.TROPHY.append(item[1:])
            elif item[0].upper() == "SCHOOL_PLAQUE":
                self.PLAQUE.append(item[1:])
            else:
                print("LINE IS INVALID (NOT SCHOOL_TROPHY OR SCHOOL_PLAQUE", item)
        self.trophyp = collections.deque(self.trophy_points)
        self.plaquep = collections.deque(self.plaque_points)

    @staticmethod
    def pop_or_default(deque, default):
        if deque:
            return deque.popleft()
        else:
            return default


    @staticmethod
    def check_size(iterable, size):
        for i in iterable:
            assert i <= size
        return iterable

    def eval_trophy(self, filename='output', outpath='', outline=False, simulate=False):
        iterator = iter(self.TROPHY)
        try:
            while True:
                if isinstance(filename, list) or isinstance(outpath, list):
                    print("HI")
                trophy.csv_to_trophy(iterator,filename,outpath,outline=outline,
                                     validpoints=self.pop_or_default(self.trophyp, (0,1,2,3,4,5,6,7,8,9)),
                                     simulate=simulate)
        except StopIteration:
            pass

    def eval_plaque(self, filename='output', outpath='', outline=False, simulate=False):
        iterator = iter(self.PLAQUE)
        try:
            while True:
                plaque.csv_to_plaque(iterator,filename,outpath,outline=outline,
                                     validpoints=self.pop_or_default(self.plaquep, plaque.PLAQUE_DEFAULT),
                                     simulate=simulate)
        except StopIteration:
            pass


class InputHolder:
    def __init__(self, path):
        self.path = os.path.expanduser(path)

        try:
            self.file = open(self.path)
        except FileNotFoundError:
            raise ArgumentTypeError("Path not found!")
        except IOError:
            raise ArgumentTypeError("The File cannot be opened! Insufficent Permissions")


    def __repr__(self):
        return "InputHolder{" + str(self.path)+"}"

    def close(self):
        self.file.close()


def make_parser():
    """Parse all the args required for the parser!"""
    parser = ArgumentParser(description="Draw school awards!", prog='Awards Generator',formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o',"--outline", help="Draws an outline template", action='store_true', default=False)
    parser.add_argument('-d',"--delete-csv", help="Deletes the csv file after successful reading", action='store_true', default=False)

    parser.add_argument('-s',"--simulate", help="Do not create output files", action='store_true', default=False)
    parser.add_argument('-oc', "--oldcsv", help="Use old 2-line csv files", action='store_true', default=False)
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-t', "--txt", help="Force read as formatted txt file", action='store_true', default=False)
    group.add_argument('-c', "--csv", help="Force read as csv file", action='store_true', default=False)

    parser.add_argument('-n',"--filename", metavar="str",nargs=1,type=str, help="Set the filename of the output file", default='output.dxf')
    parser.add_argument('-f',"--fileout", metavar='Path', nargs=1, type=str, help="Set the output path of the output file", default='')

    parser.add_argument("InputPath", help="Input Path for csv/text file in", type=InputHolder, nargs=1)
    return parser


def parse_parser(namespace):
    """Parse-ception!"""
    # get the extension
    if isinstance(namespace.filename, list):
        namespace.filename = namespace.filename[0]
    if isinstance(namespace.fileout, list):
        namespace.fileout = namespace.fileout[0]


    f = namespace.InputPath[0].file
    path = namespace.InputPath[0].path
    if namespace.csv:
        ext = 'csv'
    elif namespace.txt:
        ext = 'txt'
    elif path.endswith('txt'):
        ext = 'txt'
    elif path.endswith('csv'):
        ext = 'csv'
    elif 'csv' in path:
        ext = 'csv'
    elif 'txt' in path:
        ext = 'txt'
    else:
        ext = 'csv'
    assert isinstance(namespace.filename, str)
    assert isinstance(namespace.fileout, str)
    if ext == 'csv':
        csv_reader = CsvFileParser(f, True)
        csv_reader.eval_trophy(filename=namespace.filename,
                               outpath=namespace.fileout,
                               outline=namespace.outline,
                               simulate=namespace.simulate
                               )
        csv_reader.eval_plaque(filename=namespace.filename,
                               outpath=namespace.fileout,
                               outline=namespace.outline,
                               simulate=namespace.simulate
                               )
    else:
        csv_reader = CsvFileParser(f)
        csv_reader.eval_trophy(filename=namespace.filename,
                               outpath=namespace.fileout,
                               outline=namespace.outline,
                               simulate=namespace.simulate
                               )

if __name__ == "__main__":
    parse_parser(make_parser().parse_args())
    import time
    time.sleep(1)
