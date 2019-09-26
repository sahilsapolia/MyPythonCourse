import sys

word_list = []
for x in range(2,len(sys.argv)):
    if len(sys.argv[x]) > int(sys.argv[1]):
        word_list = word_list.append(str(sys.argv[x]))

print(list)
        