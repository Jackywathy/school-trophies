import os,sys
from argparse import ArgumentTypeError, ArgumentParser, ArgumentDefaultsHelpFormatter
import csv
import collections
import trophy, plaque
class TxtParser:
    def __init__(self, fileobj):
        self.trophy_points = []
        self.plaque_points = []
        self.csv = []
        self.current = None
        for line in fileobj:
            proc = line.rstrip()
            if proc.replace(' ',''):
                if proc.startswith("{CSV}"):
                    self.current = self.csv
                elif proc.startswith("{TROPHY_LIMITER}"):
                    self.current = self.trophy_points
                elif proc.startswith("{PLAQUE_LIMITER}"):
                    self.current = self.plaque_points
                else:
                    self.current.append(proc)
        self.trophy_points = [self.check_size(tuple(map(int,i.split())), 9) for i in self.trophy_points]
        self.plaque_points = [self.check_size(tuple(map(int,i.split())), 9) for i in self.plaque_points]
        csv_obj = csv.reader(self.csv)
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
                trophy.csv_to_trophy(iterator,filename,outpath,outline=outline,
                                     validpoints=self.pop_or_default(self.trophyp, (0,1,2,3,4,5,6,7,8,9)),
                                     simulate=simulate)
        except StopIteration:
            pass









class InputHolder:
    def __init__(self, path):
        self.path = os.path.expanduser(path)

        try:
            self._file = open(self.path)
        except FileNotFoundError:
            raise ArgumentTypeError("Path not found!")
        except IOError:
            raise ArgumentTypeError("The File cannot be opened")


    def __repr__(self):
        return "InputHolder{" + str(self.path)+"}"

    def close(self):
        self._file.close()


def parse_args():
    """Parse all the args required for the parser!"""
    global parser
    parser = ArgumentParser(description="Draw school trophies", prog='Trophy Generator',formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-outline", help="Draws an outline template", action='store_true', default=False)
    #parser.add_argument("-interact", help="Allows interactive input", action='store_true', default=False)
    parser.add_argument("-delete-csv", help="Deletes the csv file after successful reading", action='store_true', default=False)
    parser.add_argument("-filename", metavar="str",nargs=1,type=str, help="Set the filename of the output file", default='output.dxf')
    parser.add_argument("-fileout", metavar='Path', nargs=1, type=str, help="Set the output path of the output file", default='')
    parser.add_argument("-simulate", help="Do not create output files", action='store_true', default=False)
    parser.add_argument("-oldcsv", help="Use old 2-line csv files", action='store_true', default=False)
    parser.add_argument("-force-txt", help="Force read as formatted txt file", action='store_true', default=False)
    parser.add_argument("-force-csv", help="Force read as csv file", action='store_true', default=False)

    parser.add_argument("InputPath", help="Input Path for csv/text file in", type=InputHolder, nargs=1)

    #arguments = parser.parse_args()
def parse_parser(namespace):
    """Parse-ception!"""
    # get the extension
    if namespace.force_csv:
        ext = 'csv'
    elif namespace.force_txt:
        ext = 'txt'
    elif namespace.InputPath.lower().endswith('txt'):
        ext = 'txt'
    elif namespace.InputPath.lower().endswith('csv'):
        ext = 'csv'
    else:
        ext = 'csv'
    print(namespace.InputPath[0], type(namespace.InputPath[0]))
    f = namespace.InputPath[0]._file
    if ext == 'csv':
        trophy.csv_to_trophy(csv.reader(f),
                             filename=namespace.filename,
                             outpath=namespace.fileout,
                             outline=namespace.outline,
                             simulate=namespace.simulate
                             )
    else:
        txt_reader = TxtParser(f)
        txt_reader.eval_trophy(filename=namespace.filename,
                               outpath=namespace.fileout,
                               outline=namespace.outline,
                               simulate=namespace.simulate
                               )



if __name__ == "__main__":
        parse_args()
        parse_parser(parser.parse_args())


x = TxtParser(open(os.path.expanduser("~/desktop/input.txt")))
#x.eval_trophy()