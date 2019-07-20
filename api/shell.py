from datetime import datetime

from PyCli.api.exceptions import *
from PyCli.api.getchar import GetChar
from PyCli.api.tree import PyCliTree
from PyCli.api.icmds import PyCliInternalCmds

class PyCliShell(object):
    __cli_tree = None
    __prompt = "Prompt"
    __prompt_terminator = "#"
    __mode = ""
    __cli_history = []
    DEBUG = False

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
    
    def handle_help(self, cli):
        tokens = list(filter(None, cli.split(" ")))
        nois = False
        
        if len(tokens) > 0 and tokens[0] == "no":
            nois = True
            tokens = tokens[1:]
        try:
            for hp in self.cli_tree.find_all_help(tokens, nois):
                self.print_realtime("\n %-20s %s" %(hp["name"], hp["help"]))
        except Exception as e:
            #raise e
            self.print_realtime("\nInvalid CLI: %s"%cli)
        self.print_realtime("\n")
    
    def handle_internal_cr(self, ex, nois=False):
        return getattr(PyCliInternalCmds, ex)(self, nois=nois)
        
    def handle_cr(self, cli):
        tokens = list(filter(None, cli.split(" ")))
        nois = False
        if len(tokens) > 0 and tokens[0] == "no":
            nois = True
            tokens = tokens[1:]
        try:
            ex = self.cli_tree.find_executable(tokens, nois)
            if ex is None:
                self.print_realtime("\nInvalid CLI: %s"%cli)
                
            if ex[1] is "pycli_internal":
                self.handle_internal_cr(ex[0], ex[2])
            else:
                self.handle_external_cr(ex[0], ex[2])
            
        except Exception as e:
            #raise e
            self.print_realtime("\nCLI Not Implemented: %s"%(cli))
        self.print_realtime("\n")
        
    def attach(self):
        curr_cli = ""
        term = GetChar()
        while True:
            PyCliShell.print_realtime("\n%s" % (self.get_prompt_string()), curr_cli)
            while True:
                uchar = term.stdin()
                if uchar is '?':
                    PyCliShell.print_realtime(uchar)
                    self.handle_help(curr_cli)
                    break
                if uchar is '\n' or uchar is '\r':
                    ccli = curr_cli.strip()
                    curr_cli = ""
                    if ccli is not "":
                        now = datetime.now()
                        self.print_realtime("\n-- %s -- \n" % now)
                        self.cli_history.insert(0, (str(now), ccli))
                        self.handle_cr(ccli)
                    PyCliShell.print_realtime("")
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
                    uchar = term.stdin()
                    uchar = term.stdin()
                    if uchar is 'A':
                        if self._up_count < len(self.cli_history):
                            curr_cli = self.cli_history[self._up_count][1]
                            self._up_count += 1
                    break
                if uchar is '\x03':
                    PyCliShell.print_realtime("\n")
                    curr_cli = ""
                    break;
                curr_cli += uchar
                if self.DEBUG:  
                    PyCliShell.print_realtime("'%d',"%ord(uchar))
                else:
                    PyCliShell.print_realtime(uchar)
                self._up_count = 0


def pyclishell_ut():
    from PyCli.api.parser import PyCliParser
    from PyCli.api.node import PyCliNodeBuilder
    pcp = PyCliParser(".")
    nodes = pcp.parse(pcp.find())
    tree = PyCliTree()
    tree.attach(nodes)
    shell = PyCliShell(tree)
    shell.attach()


if __name__ == "__main__":
    pyclishell_ut()