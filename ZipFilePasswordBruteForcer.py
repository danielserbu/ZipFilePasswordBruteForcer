import zipfile
import sys

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ZipFilePasswordBruteForcer")
    parser.add_argument("zipfile", help="ZIP File to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contains password list on each line.")

    args = parser.parse_args()
    zip_file = zipfile.ZipFile(args.zipfile)
    passlist = open(args.passlist).read().split("\n")
    for password in passlist:
        password = password.strip("\n").encode()
        try:
            sys.stdout.write("\n[X] Attempting password -> {}\r".format(password.decode()))
            files_in_zip = zip_file.namelist()
            # Try to open first file in the zip array.
            zip_file.open(files_in_zip[0], pwd=bytes(password))
        except Exception as e:
            continue
        else:
            sys.stdout.write("\n[>>>>>] Valid password '{}' found!\n".format(password.decode()))
            exit(0)
    sys.stdout.write("\n\tNo password found\n")
