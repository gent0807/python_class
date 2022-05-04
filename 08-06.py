LCD=[[ "|||||",
       "|   |",
       "|   |",
       "|   |",
       "|||||"
        ],
      ["    |",
       "   ||",
       "    |",
       "    |",
       "  ||||"],
      ["|||||",
       "    |",
       "|||||",
       "|    ",
       "|||||"],
      ["|||||",
       "    |",
       "|||||",
       "    |",
       "|||||"],
      ["|   |",
       "|   |",
       "|||||",
       "    |",
       "    |"],
      ["|||||",
       "|    ",
       "|||||",
       "    |",
       "|||||"],
      ["|    ",
       "|    ",
       "|||||",
       "|   |",
       "|||||"],
      ["|||||",
       "|   |",
       "    |",
       "    |",
       "    |"],
      ["|||||",
       "|   |",
       "|||||",
       "|   |",
       "|||||"],
      ["|||||",
       "|   |",
       "|||||",
       "    |",
       "    |"]
     ]
ROW=5
def printLCD(digit):
    for row in range(ROW):
        for i in range(len(digit)):
            num=int(digit[i])
            print(LCD[num][row], end=' ')
        print()
def checkdgt(s):
    tag=True
    for c in s:
        if c not in '0123456789':
            tag=False
            break
        return tag
snum= '11'
snum=input("0~9 자릿수로만 정수형태 1개 입력>>")
printLCD(snum)
