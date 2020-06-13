#!/usr/bin/env python3
# requires python 3.x  
import random
boggleDie = [['Q','B','Z','J','X','K'],['T','O','U','O','T','O'],['O','V','W','R','G','R'],['A','A','A','F','S','R'],['A','U','M','E','E','G'],
        ['H','H','L','R','D','O'],['N','H','D','T','H','O'],['L','H','N','R','O','D'],['A','F','A','I','S','R'],['Y','I','F','A','S','R'],
        ['T','E','L','P','C','I'],['S','S','N','S','E','U'],['R','I','Y','P','R','H'],['D','O','R','D','L','N'],['C','C','W','N','S','T'],
        ['T','T','O','T','E','M'],['S','C','T','I','E','P'],['E','A','N','D','N','N'],['M','N','M','E','A','G'],['U','O','T','O','W','N'],
        ['A','E','A','E','E','E'],['Y','I','F','P','S','R'],['E','E','E','E','M','A'],['I','T','I','T','I','E'],['E','T','I','L','I','C']]
boggleBoard = []
boggleColumn = []
dieOrder = []
incr = 0
while len(dieOrder) < 25:
    incr+=1
    r = random.randint(0,24)
    if r not in dieOrder:
        dieOrder.append(r)
#        print(dieOrder)
count = 0
column = 0
for x in range(0,25):
    boggleColumn.append(boggleDie[dieOrder[x]][random.randint(0,5)])
    count+=1
    if count == 5:
        boggleBoard.append(boggleColumn)
        column+=1
        count = 0
        boggleColumn = []
#print(incr)
#print()
#print()
#for x in boggleBoard:
#    print(x)

r = 5
c = 5

myfile = open("BoggleBoard.html",'w')

print("<style type=\"text/css\">  \
.tg  {border-collapse:collapse;border-spacing:0;} \
.tg td{border-color:black;border-style:solid;border-width:2px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;word-break:normal;} \
.tg td{border-color:black;border-style:solid;border-width:2px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 20px;word-break:normal;} \
.tg .tg-k3zs{border-color:inherit;font-family:\"Courier New\", Courier, monospace !important;;font-size:72px;font-weight:bold;text-align:center;vertical-align:center} \
</style>",file=myfile)

print("<table class=\"tg\">", file=myfile)

for i in range(0,c):
    print("<tbody>", file=myfile)
    print(" <tr>", file=myfile)
    for j in range(0,r):
        print("  <td class=\"tg-k3zs\">{}</td>".format(boggleBoard[i][j]), file=myfile)
    print(" </tr>", file=myfile)
    print("</tbody>", file=myfile)

print("</table>", file=myfile)

myfile.close()

