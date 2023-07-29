import os
import hashlib
from send2trash import send2trash

hashes = []

# https://www.programiz.com/python-programming/examples/hash-file
def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   digest = h.hexdigest()
   return digest

# To whatever poor soul has to read this jenky disgusting code
# I sincerely apologize, I'm in a rush

def main():
    path = input("Enter a file directory: ")
    x = 0 # Total number of files
    for root, direc, files in os.walk(path):
        x += len(files)
    print(f'Recursively searching {x} files.')

    i = 0 # File index
    for root, direc, files in os.walk(path):
        for f in files:
            i += 1
            print(f'Checking file {i}/{x}.')
            file = os.path.join(root, f)
            digest = hash_file(file)
            if digest in hashes:
                print(f'Removing duplicate {file}.')
                send2trash(file)
            else:
                hashes.append(digest)

if __name__ == '__main__':
    main()
