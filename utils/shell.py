from PyCLI.exceptions import *
from PyCLI.utils.getchar import GetChar

class PyCliTree:
    pass

class PyCliShell:
    __cli_tree = None
    __prompt = "Prompt"
    __prompt_terminator = "#"
    __mode = ""
    __cli_history = []
    __debug = False


    _up_count = 0
    
    def __init__(self,
                 cli_tree,
                 prompt="Prompt",
                 prompt_terminator="#",
                 mode = None):

        self.cli_tree           = cli_tree
        self.prompt             = prompt
        self.prompt_terminator  = prompt_terminator
        self.mode               = mode

    @property
    def cli_tree(self):
        return self.__cli_tree

    @cli_tree.setter
    def cli_tree(self, cli_tree):
        if isinstance(cli_tree, PyCliTree):
            self.__cli_tree = cli_tree
        else:
            raise PyCliTypeError("cli_tree", PyCliTree)

    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt):
        self.__prompt = prompt
    
    @property
    def prompt_terminator(self):
        return self.__prompt_terminator

    @prompt_terminator.setter
    def prompt_terminator(self, prompt_terminator):
        if isinstance(prompt_terminator, str):
            if len(prompt_terminator) == 1:
                self.__prompt_terminator = prompt_terminator
            else:
                raise PyCliValueError(
                    "Expected length of prompt_terminator is 1")
        else:
            raise PyCliTypeError("prompt_terminator", str)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode
    
    @property
    def cli_history(self):
        return self.__cli_history

    @cli_history.setter
    def cli_history(self, cli_history):
        self.__cli_history = cli_history
    
    @staticmethod
    def print_realtime(*args):
        print(*args, end="", flush=True)

    def get_prompt_string(self):
        retstr = "%s"%(self.prompt)
        if self.mode is not None and self.mode is "":
            retstr += "(%s)" % self.mode
        retstr += self.prompt_terminator
        return retstr

    def attach(self):
        curr_cli = ""
        while True:
            PyCliShell.print_realtime("\n%s" % (self.get_prompt_string()), curr_cli)
            while True:
                uchar = GetChar.stdin()
                if uchar is '?':
                    PyCliShell.print_realtime(uchar)
                    break
                if uchar is '\n' or uchar is '\r':
                    if curr_cli.strip() is not "":
                        self.cli_history.insert(0, curr_cli.strip())
                    if curr_cli == "history":
                        print("")
                        print(self.cli_history)
                    if curr_cli == "debug keystrokes":
                        print("")
                        self.__debug = True
                    if curr_cli == "undebug keystrokes":
                        print("")
                        self.__debug = False

                    PyCliShell.print_realtime("")
                    curr_cli = ""
                    break 
                if uchar is '\t':
                    PyCliShell.print_realtime("TAB\n")
                    curr_cli = ""
                    break
                if uchar is '\x7f':
                    if curr_cli is "":
                        continue
                    PyCliShell.print_realtime("\b \b")
                    curr_cli = curr_cli[:-1]
                    continue
                if uchar is '\x1b':
                    uchar = GetChar.stdin()
                    uchar = GetChar.stdin()
                    if uchar is 'A':
                        if self._up_count < len(self.cli_history):
                            curr_cli = self.cli_history[self._up_count]
                            self._up_count += 1
                    break
                if uchar is '\x03':
                    PyCliShell.print_realtime("\n")
                    exit(0)
                curr_cli += uchar
                if self.__debug:
                    PyCliShell.print_realtime(ord(uchar))
                else:
                    PyCliShell.print_realtime(uchar)
                self._up_count = 0


a = PyCliShell(PyCliTree())
a.attach()
