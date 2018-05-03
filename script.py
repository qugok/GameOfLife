#!/usr/bin/python

import getopt
import sys

from Life import Game


def getInput(filename, steps):
    if filename == '':
        print("Please write count of steps\n")
        steps[0] = int(input())
        print("Please write ocean size (hight, witdh)\n")
        hight, witdh = map(int, input().split())
        print("Please write the ocean\n")
        field = []
        for i in range(hight):
            field.append(list(input()))
        # print(field)
        return field
    else:
        with open(filename, 'r') as f:
            steps[0] = int(f.readline())
            hight, witdh = map(int, f.readline().split())
            field = []
            for i in range(hight):
                field.append(list(*f.readline().split()))
            # print(field)
            return field


def output(game, outputfile=''):
    if outputfile == '':
        print(game)
    else:
        with open(outputfile, 'w') as f:
            f.write(str(game))


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "h:i:o:", ["help", "ifile=", "ofile="])
    except getopt.GetoptError:
        print('incorrect command, please use flag -h/--help to read how to use Life')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('script.py\n-i\t--ifile\t<inputfile>\n-o\t--ofile\t<outputfile>\n-h\t--help\thelp infomation about '
                  'script')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    steps = [0]
    game = Game(getInput(inputfile, steps))
    steps = steps[0]
    game.step(steps)
    output(game, outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
