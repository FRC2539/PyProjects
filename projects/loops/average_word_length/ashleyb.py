string = input('type in a sentence or smth ')
wordlen, numword = 0, 1
for x in range(0, len(string)):
    if string[x:x + 1] == ' ':
        numword = numword + 1
    elif str[x:x + 1] == '.' or ',' or '!' or '?':
        wordlen = wordlen - 1
    else:
        wordlen = wordlen + 1
print('average: %s' % (wordlen / numword))