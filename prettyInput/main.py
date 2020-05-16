import sys


def read_int(stream=sys.stdin) -> int:
    value = ''
    while True:
        sym = stream.read(1)
        if sym.isdigit() or (len(value) == 0 and sym == '-'):
            value += sym
        elif len(value) == 0:
            continue
        else:
            break
    try:
    	return int(value)
    except ValueError:
    	return None


def read_float(stream=sys.stdin, sep_list=('.'), allow_exp=True) -> float:
    value = ''
    e_met = False
    point_met = False
    while True:
        sym = stream.read(1)
        if sym.isdigit() or ((len(value) == 0 or value[-1] == 'e') and sym == '-'):
            value += sym
        elif sym in sep_list and not point_met and not e_met:
            point_met = True
            value += '.'
        elif sym == 'e' and not e_met and allow_exp:
            e_met = True
            value += 'e'
        elif len(value) == 0:
            continue
        else:
            break
    try:
    	return float(value)
    except ValueError:
    	return None


def read_str(stream=sys.stdin, end_list=('\x1a', '\n')) -> float:
    string = ''
    while True:
        char = stream.read(1)
        if char in end_list:
            break
        else:
            string += char
    return string


class StreamIO:
    def __init__(self, stream=sys.stdin):
        self.stream = stream

    def read_int(self):
        return read_int(self.stream)

    def read_float(self, sep_list=('.'), allow_exp=True):
        return read_float(self.stream, sep_list, allow_exp)

    def read_str(self, end_list=('\x1a', '\n')):
        return read_str(self.stream, end_list)

    def write(self, data):
        self.stream.write(data)

    def close(self):
        self.stream.close()

    def writable(self):
        return self.stream.writable()

    def readable(self):
        return self.stream.readable()

    @staticmethod
    def from_file(path, mode):
        return StreamIO(open(path, mode))