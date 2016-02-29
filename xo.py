#! /usr/bin/python

table=[[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
def showTable(table):
	print '{0:2} {1:2} {2:2}'.format(table[0][0],table[0][1],table[0][2])
	print '{0:2} {1:2} {2:2}'.format(table[1][0],table[1][1],table[1][2])
	print '{0:2} {1:2} {2:2}'.format(table[2][0],table[2][1],table[2][2])

def chTable(piece):
	print ''
	input=int(raw_input("input:"))-1
	print ''
	i=input/3
	j=input%3
	if table[i][j]==" ":
		table[i][j]=piece
	else:
		print 'error,please input again.'
		print ''
		chTable(piece)

def checkWinner(piece):
	if (table[0][0]==table[0][1] and table[0][0]==table[0][2] and tbale[0][0]==piece) or (table[1][0]==table[1][1] and table[1][0]==table[1][2] and table[1][0]==piece) or (table[2][0]==table[2][1] and table[2][0]==table[2][2] and table[2][0]==piece) or (table[0][0]==table[1][0] and table[0][0]==table[2][0] and table[0][0]==piece) or (table[0][1]==table[1][1] and table[1][1]==table[2][1] and table[0][1]==piece) or (table[0][2]==table[1][2] and table[0][2]==table[2][2] and table[0][2]==piece) or (table[0][2]==table[1][1] and table[0][2]==table[2][0] and table[0][2]==piece) or (table[0][0]==table[1][1] and table[0][0]==table[2][2] and table[0][0]==piece):
		print 'winner is:'+piece+'!'
		return 1
	else:
		return 0

def playGame():
	for i in range(9):
		if i%2==0:
			piece="x"
			chTable(piece)
			showTable(table)
			if checkWinner(piece)==1:
				break
		else:
			piece="o"
			chTable(piece)
			showTable(table)
			if checkWinner(piece)==1:
				break

print 'please input number 1-9'
showTable(table)
playGame()
print ''
print 'draw!'
