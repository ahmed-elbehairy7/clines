#!/usr/bin/python


from sys import exit
from argparse import ArgumentParser
import os
import re

parser = ArgumentParser(description="Application for counting lines in files")
parser.add_argument("file_path", action="append", help="The path for the file to count lines")
parser.add_argument("-i", "--ignore", metavar="", action="append", help="Files or dirs to ignore", default=["^\/?(?:[^/]+\/)*(\.[^/]+)$", "node_modules", "^.*\.(jpg|json|mp4|MP4|jpeg|JPG|gif|GIF|doc|DOC|pdf|PDF|lnk|png|bak|pypam|pam|log|hex|csv|txt|exe)$", "__pycache__", "package-lock.json"])
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

if args.verbose:
    verprint = print
else:
    verprint = lambda x : x


def main():
    code_count = 0
    
    files = get_paths(args.file_path)
    if len(args.file_path) == 1:
        project_name = os.path.split(args.file_path[0])[-1]
    else:
        project_name = "unknown"
    
    space_lines = 0
    comments_sum = 0
    sum = 0
    files_num = 0
    for file in files:
        files_num += 1
        verprint(f"Currently at file {file}")
        code_count = 0
        comments = 0
        try:
            with open(file, encoding='utf-8') as f:
                for line in f.readlines():
                    if line.strip().lower().startswith(('#', '//', '/*', '*/', '"""', '--', "*", "@rem")):
                        comments += 1
                        continue
                    if not line.isspace():
                        code_count += 1
                        continue
                    space_lines += 1
        except FileNotFoundError:
            exit("File not found")
        
        sum += code_count
        comments_sum += comments
        print(f"Lines in {file}: {code_count}")
        verprint(f"comments in {file}: {comments}")

    print(f"\n\nLines in {project_name}:\n")
    print(f"Sum of code lines: {sum}")
    print(f"Sum of comments: {comments_sum}")
    print(f"sum of lines written in the project: {sum + comments_sum}")
    print(f"number of files: {files_num}")
    print(f"White space lines: {space_lines}")
    
def get_paths(paths):
    new = []
    for ignore in args.ignore:
        r = re.compile(ignore)
        paths = list(filter(lambda x : not r.match(os.path.split(x)[-1]), paths))
        
    for file in paths:
        if os.path.isdir(file):
            new += get_paths(map(lambda x : os.path.join(file, x), os.listdir(file)))
            continue
        new.append(file)
    
    return new


if __name__ == "__main__":
    main()
