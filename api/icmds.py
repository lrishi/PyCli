""" PyCli Base CLI Commands """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


class PyCliInternalCmds():
    """ Internal CLI Commands """

    @staticmethod
    def pycli_exit(clss, nois):
        """ Prompt# quit """
        #pylint: disable=unused-argument
        exit(0)

    @staticmethod
    def pycli_debug_keystrokes(clss, nois):
        """ Prompt# [no] debug keystrokes """
        if nois is True:
            clss.DEBUG = False
        else:
            clss.DEBUG = True

    @staticmethod
    def pycli_show_tree(clss, nois):
        """ Prompt# show cli-tree """
        #pylint: disable=unused-argument
        clss.print_realtime("\n", str(clss.cli_tree))

    @staticmethod
    def pycli_show_history(clss, nois):
        """ Prompt# show history """
        #pylint: disable=unused-argument
        clss.print_realtime("\n")
        header = True
        for hist in clss.cli_history:
            if header is True:
                header = False
                clss.print_realtime("\n %-35s %s" % ("Timestamp", "Command"))
                clss.print_realtime("\n %-35s %s" % ("----------", "--------"))

            clss.print_realtime("\n %-35s %s" % (hist[0], hist[1]))
