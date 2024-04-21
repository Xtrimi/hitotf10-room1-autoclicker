import argparse
#import cv2
#import numpy as np
import os
import pyautogui
import pydirectinput
import sys
import time

pydirectinput.PAUSE=1 #TODO: 0.01 is too fast
THRESHOLD = 30
SYMBOLS = "→↗↑↖←↙↓↘"
DIRECTIONS = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]
#FOUND = ['000000010', '0000001111', '0000010011', '00001101', '00001110', '0010100000', '001100000', '00110011', '00111101', '001111100', '01000101', '010010101', '01001011', '0101000001', '01010110', '0101111010', '011001001', '011011001', '011011101', '011011111', '011101110', '0111100100', '011111011', '1000011001', '10001011', '1001000110', '10010110', '10010111', '100110001', '10011001', '1010000010', '1010010010', '101101101', '10111000', '101110010', '110000010', '11000101', '110011101', '1101000010', '11010111', '1101100000', '1101100011', '11101011', '1111010011', '1111101001', '1111111010']
#FIND = ['0111001100']

w = None
def focus():
    w = pyautogui.getWindowsWithTitle("Roblox")[0]
    w.maximize()
    w.activate()
    time.sleep(1)

def click(i, j):
    start = (542, 78)
    increment = 19

    x = start[0] + (i-1)*increment + 4*(i//14)
    y = start[1] + (j-1)*increment + 4*(j//14)
    pydirectinput.click(x, y)

def autoclick():
    if not os.path.isfile('grid.txt'):
        print("Error: File grid.txt does not exist")
        sys.exit(1)
    if not os.path.isfile('answer.txt'):
        print("Error: File answer.txt does not exist")
        sys.exit(1)
    focus()

    with open('answer.txt', encoding='utf-8') as f:
        for line in f:
            line = line[:-1].split('\t')
            #print(line)
            #if line[0] in FOUND:
            #    continue
            #if not line[0] in FIND:
            #    continue
            length = len(line[0])
            y = int(line[1])
            x = int(line[2])
            dir = SYMBOLS.index(line[3])
            #print(x, y)
            #print(length, x, y, dir)
            click(x, y)
            print(line)
            input("continue")
            #click(x + (length-1)*DIRECTIONS[dir][0], y + (length-1)*DIRECTIONS[dir][1])

def read():
    print("broken lmao dont run this")
    sys.exit(1)

    '''if os.path.isfile('grid.txt'):
        print("Error: grid.txt already exists, please remove if you want to perform this action")
        sys.exit(1)
    focus()

    im = pyautogui.screenshot()
    im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    im = im[68:1030, 531:1494] #U:D, L:R

    _, im = cv2.threshold(im, THRESHOLD, 255, cv2.THRESH_BINARY)
    #cv2.imwrite("test.jpg", im)
    contours, _ = cv2.findContours(im, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) <= 10:
            continue    
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255,0), 2)
        center = (x,y)
        #print (center)

    cv2.imwrite("resul3.jpg", im)'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest='cmd_name')
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-r', '-R', '-read', dest='read', action='store_true',
                        help='(BROKEN) Reads only the grid and outputs into grid.txt. Cannot read list of words.' )
    g.add_argument('-a', '-A', '-auto', '-autoclick', dest='autoclick', action='store_true',
                        help='''Autoclicks words based on grid.txt and answer.txt. Must have these two text files.
answer.txt - Transcribe the word list and paste it into https://www.dcode.fr/word-search-solver.
Then, click the clipboard button and remove the first line and last two lines (arrows, N count and empty line).''')
    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.read:
        read()
    elif args.autoclick:
        autoclick()