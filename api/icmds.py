

class PyCliInternalCmds(object):
    
    @staticmethod
    def pycli_exit(clss, nois):
        exit(0)
    
    @staticmethod
    def pycli_debug_keystrokes(clss, nois):
        if nois == True:
            clss.DEBUG = False
        else:
            clss.DEBUG = True
        
    @staticmethod
    def pycli_show_tree(clss, nois):
        clss.print_realtime("\n", str(clss.cli_tree))
            
    @staticmethod
    def pycli_show_history(clss, nois):
        clss.print_realtime("\n")
        header = True
        for hist in clss.cli_history:
            if header is True:
                header = False
                clss.print_realtime("\n %-35s %s" % ( "Timestamp", "Command" ))
                clss.print_realtime("\n %-35s %s" % ( "----------", "--------" ))
                
            clss.print_realtime("\n %-35s %s" % (hist[0], hist[1]))