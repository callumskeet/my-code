#! python3
# madLibs.py - opens .txt files containing senteces with placeholder text (e.g.
# ADJECTIVE) and replaces them with user-supplied strings.

import re
import os

os.chdir('madLibs')

while True:
    print('Choose a mad lib:')
    for filename in os.listdir():
        if '.txt' in filename:
            print(' * ' + filename.strip('.txt'))
    madLibFile = input().lower()
    madLibFileTxt = madLibFile + '.txt'
    unedited = open('.\\' + madLibFileTxt)
    unedited = unedited.read()
    print('\nPreview Mad Lib (Y/N)?')
    if input().lower().startswith('y'):
        print('\n' + unedited)

    print()
    wordList = re.findall(r"[\w']+|[.,!?;]", unedited)

    for i in range(len(wordList)):
        if wordList[i] == 'ADVERB':
            print('Enter an adverb:')
            wordList[i] = input()
        elif wordList[i] == 'ADJECTIVE':
            print('Enter an adjective:')
            wordList[i] = input()
        elif wordList[i] == 'NOUN':
            print('Enter a noun:')
            wordList[i] = input()
        elif wordList[i] == 'VERB':
            print('Enter a verb:')
            wordList[i] = input()

    i = 0
    while i < len(wordList):
        if wordList[i] == '.':
            wordList[i - 1] = wordList[i - 1] + wordList[i]
            del wordList[i]
        i += 1

    madLib = ' '.join(wordList)
    print(madLib)
    print('\nWould you like to save this mad lib (Y/N)?')
    saveQ = input()
    if saveQ.lower().startswith('y'):
        finalMadLib = open('.\\saved\\' + madLibFile + '_edited.txt', 'w')
        finalMadLib.write(madLib)
        finalMadLib.close()
        print('\nYour mad lib has been saved to your computer.\n')
    print('Try another mad lib (Y/N)?')
    if input().lower().startswith('y'):
        print()
        continue
    else:
        break
