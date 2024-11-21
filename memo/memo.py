# memo.py
import sys

option = sys.argv[1]
filename = sys.argv[2]

if option == '-a':
    memo = sys.argv[3]
    f = open(filename, 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f= open(filename)
    memo = f.read()
    f.close()
    print(memo)
