import sys

def handleDepthRecursively(args):
    if args[4].isdigit():
        if len(args) > 6 and args[5] == "-p":
            print("with path")
        else:
            print("without path")
    else:
        print("Invalid depth level")
        print("use -h to see help section")
        sys.exit()

def handleRecursively(args):
    print("recursively download")
    if len(args) > 3 and args[2] == "-p":
        print("with path")
    else:
        print("without path")

def check_args(args):
    if len(args) == 1:
        print("use -h to see help sction.")
        sys.exit()

    if args[1] not in ['-r', '-p']:
        print('Invalid arguments')
        print('use -h to see help section')
        sys.exit()

def handleArgs(args):
    if args[1] == "-h":
        print('''/spider [-rlp] URL
    • Option -r : recursively downloads the images in a URL received as a parameter.
    • Option -r -l [N] : indicates the maximum depth level of the recursive download.
    If not indicated, it will be 5.
    • Option -p [PATH] : indicates the path where the downloaded files will be saved.
    If not specified, ./data/ will be used.''')
        sys.exit()

    if len(args) > 2 and args[1] == "-r":
        if len(args) > 5 and args[2] == "-l":
            handleDepthRecursively(args)
        else:
            handleRecursively(args)


if __name__ == "__main__":
    args = sys.argv
    check_args(args)
    handleArgs(args)
