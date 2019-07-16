from GetChar import GetChar


class CliNode:
    _string = "Unknown"
    _next   = [] 
    _attributes = []

    def __init__(self, _string):
        self._string = _string
    
    def __str__(self):
        return self._string

cli_tree = {
    "show": {
        "context": CliLeaf("show_context"),
        "version": CliLeaf("show_version"),
        "controller": {
            "pse": {
                "statistics": {
                    "instance": CliIntegerBud("instance", next= {
                    })
                }
            }
        }
    }

}

curr_cli = ""
cli_history = []

while True:
    print("\nPrompt#", curr_cli, end="", flush=True)
    while True:
        uchar = GetChar.stdin()
        if uchar is '?':
            print(uchar, end="", flush=True)
            break
        if uchar is '\n' or uchar is '\r':
            cli_history.append(curr_cli)
            if curr_cli == "history":
                print("")
                print(cli_history)
            print("", end="", flush=True)
            curr_cli = ""
            break 
        if uchar is '\t':
            print("TAB")
            curr_cli = ""
            break
        if uchar is '\x7f':
            if curr_cli is "":
                continue
            print("\b \b", end="", flush=True)
            curr_cli = curr_cli[:-1]
            continue
        if uchar is '\x03':
            print("\n", flush=True)
            exit(0)
        curr_cli += uchar
        print(uchar, end="", flush=True)

