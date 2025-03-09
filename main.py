import subprocess, re, random, os, sys
from turtledemo.sorting_animate import enable_keys

libFolder = ''
tgtFolder = ''
pipPath = ''


# A python class definition for printing formatted text on terminal.
# Initialize TextFormatter object like this:
# >>> cprint = TextFormatter()
#
# Configure formatting style using .cfg method:
# >>> cprint.cfg('r', 'y', 'i')
# Argument 1: foreground(text) color
# Argument 2: background color
# Argument 3: text style
#
# Print formatted text using .out method:
# >>> cprint.out("Hello, world!")
#
# Reset to default settings using .reset method:
# >>> cprint.reset()

class TextFormatter:
    COLORCODE = {
        'k': 0,  # black
        'r': 1,  # red
        'g': 2,  # green
        'y': 3,  # yellow
        'b': 4,  # blue
        'm': 5,  # magenta
        'c': 6,  # cyan
        'w': 7   # white
    }
    FORMATCODE = {
        'b': 1,  # bold
        'f': 2,  # faint
        'i': 3,  # italic
        'u': 4,  # underline
        'x': 5,  # blinking
        'y': 6,  # fast blinking
        'r': 7,  # reverse
        'h': 8,  # hide
        's': 9,  # strikethrough
    }

    # constructor
    def __init__(self):
        self.reset()


    # function to reset properties
    def reset(self):
        # properties as dictionary
        self.prop = {'st': None, 'fg': None, 'bg': None}
        return self


    # function to configure properties
    def cfg(self, fg, bg=None, st=None):
        # reset and set all properties
        return self.reset().st(st).fg(fg).bg(bg)


    # set text style
    def st(self, st):
        if st in self.FORMATCODE.keys():
            self.prop['st'] = self.FORMATCODE[st]
        return self


    # set foreground color
    def fg(self, fg):
        if fg in self.COLORCODE.keys():
            self.prop['fg'] = 30 + self.COLORCODE[fg]
        return self


    # set background color
    def bg(self, bg):
        if bg in self.COLORCODE.keys():
            self.prop['bg'] = 40 + self.COLORCODE[bg]
        return self


    # formatting function
    def format(self, string):
        w = [self.prop['st'], self.prop['fg'], self.prop['bg']]
        w = [str(x) for x in w if x is not None]
        # return formatted string
        return '\x1b[%sm%s\x1b[0m' % (';'.join(w), string) if w else string


    # output formatted string
    def out(self, string):
        print(self.format(string))


def listFilesInFolderByNameRegexExt(folderpath: str, seeknameregex: str,
                                    fileext: str, fullfilenames: bool = True):
    colorprint = TextFormatter()
    colorprint.cfg('y', 'k', 'b')
    if len(folderpath) == 0:
        colorprint.out('PATH TO FOLDER IS EMPTY')
        return None
    if not os.path.exists(folderpath):
        colorprint.out('PATH TO FOLDER DOES NOT EXIST')
        return None
    filenames = []
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            foundname = os.path.splitext(filename)[0]
            foundext = os.path.splitext(filename)[1]
            if foundext == fileext and re.match(seeknameregex, foundname):
                if fullfilenames:
                    filenames.append(os.path.join(root, filename))
                else:
                    filenames.append(filename)
    return filenames


def listFilesInFolderByNameRegex(folderpath: str, seeknameregex: str,
                                    fullfilenames: bool = True):
    colorprint = TextFormatter()
    colorprint.cfg('y', 'k', 'b')
    if folderpath == '':
        colorprint.out('PATH TO FOLDER IS EMPTY')
        return None
    if not os.path.exists(folderpath):
        colorprint.out('PATH TO FOLDER DOES NOT EXIST')
        return None
    filenames = []
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            foundname = os.path.splitext(filename)[0]
            foundext = os.path.splitext(filename)[1]
            if re.match(seeknameregex, foundname):
                if fullfilenames:
                    filenames.append(os.path.join(root, filename))
                else:
                    filenames.append(filename)
    return filenames


def listFilesInFolderByExt(folderpath: str, fileext: str = '.whl',
                           fullfilenames: bool = False):
    colorprint = TextFormatter()
    colorprint.cfg('y', 'k', 'b')
    if folderpath == '':
        colorprint.out('PATH TO FOLDER IS EMPTY')
        return None
    if not os.path.exists(folderpath):
        colorprint.out('PATH TO FOLDER DOES NOT EXIST')
        return None
    filenames = []
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            if os.path.splitext(filename)[1] == fileext:
                if fullfilenames:
                    filenames.append(os.path.join(root, filename))
                else:
                    filenames.append(filename)
    return filenames


######### SCRIPT #########
if __name__ == "__main__":
    colorprint = TextFormatter()
    colorprint.cfg('r', 'k', 'b')
    if not os.path.exists(libFolder):
        if len(sys.argv) > 1:
            if not os.path.exists(sys.argv[1]):
                colorprint.out('INCORRECT LIB FOLDER ARGUMENT SPECIFIED')
                systemExitCode = 1
                sys.exit(systemExitCode)
            else:
                libFolder = sys.argv[1]
        else:
            colorprint.out('LIB FOLDER NOT SET AND NOT SPECIFIED AS ARGUMENT')
            systemExitCode = 2
            sys.exit(systemExitCode)
    if not os.path.exists(tgtFolder):
        if len(sys.argv) > 2:
            if not os.path.exists(sys.argv[2]):
                colorprint.out('INCORRECT TARGET FOLDER ARGUMENT SPECIFIED')
                systemExitCode = 3
                sys.exit(systemExitCode)
            else:
                tgtFolder = sys.argv[2]
        else:
            colorprint.out('TARGET FOLDER NOT SET AND NOT SPECIFIED AS ARGUMENT')
            systemExitCode = 4
            sys.exit(systemExitCode)
    if not os.path.exists(pipPath):
        if len(sys.argv) > 3:
            if not os.path.exists(sys.argv[3]):
                colorprint.out('INCORRECT PIP PATH ARGUMENT SPECIFIED')
                systemExitCode = 5
                sys.exit(systemExitCode)
            else:
                pipPath = sys.argv[3]
        else:
            colorprint.out('PIP PATH DOES NOT EXIST AND NOT SPECIFIED AS ARGUMENT')
            systemExitCode = 6
            sys.exit(systemExitCode)
    liblist = listFilesInFolderByExt(libFolder)
    if len(liblist) == 0:
        colorprint.out('NO LIBS FOUND IN LIB FOLDER')
        systemExitCode = 7
        sys.exit(systemExitCode)
    for rec in liblist:
        libName = rec.split('-')[0]
        arglist = [ pipPath,
                    'download',
                    '-d',
                    tgtFolder,
                    # '"' + tgtFolder + '"',
                    libName ]
        subprocess.run(arglist)
