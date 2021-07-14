import random
import os
#initialising two lists, the first list will be the list that is printed and the second list is used in the background to check for the words

crossword=[]
crosswordx=[]

#store_list is a 2D list storing data regarding the score (dictionary can be used too)

store_list=[]
player_cnt='0'

while not(player_cnt.isdigit()) or int(player_cnt)<1:
	player_cnt=input("Enter number of players: ")
	if not(player_cnt.isdigit()) or int(player_cnt)<1:
		print("Invalid input, Try Again!")
for player in range(int(player_cnt)):
	store_list.append("")
	store_list[player]=[]

#randomly choosing a board from the list of 12 boards and opening the board

x=random.randint(0,11)
csv_list=["board_1.csv","board_2.csv","board_3.csv","board_4.csv","board_5.csv","board_6.csv","board_7.csv","board_8.csv","board_9.csv","board_10.csv","board_11.csv","board_12.csv"]
table1=open(csv_list[x],'r')

line1=table1.readline().strip().split(',')

#adding the elements to our two lists

rows=int(line1[0])
cols=int(line1[1])
for i in range(rows):
	crossword.append(table1.readline().strip().split(','))

table1.close()

for a in range(rows):
	rowx=[]
	for b in range(cols):
		rowx.append(crossword[a][b])
	crosswordx.append(rowx)

#printing the crossword for the first time

print("\n     Welcome to Word Search!!")
for j in range(rows):
	print("+"+"---+"*rows)
	print("|",end=" ")
	for k in range(cols):
			print(crossword[j][k]+" |", end=" ")
	print()

print("+"+"---+"*rows)

#functions which find and capitalise the typed words

def chec_hori_for(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r][s+inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r][s+inc])>96:
							crossword[r][s+inc]=chr(ord(crossword[r][s+inc])-32)
						inc+=1
					return True
def chec_hori_back(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r][s-inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r][s-inc])>96:
							crossword[r][s-inc]=chr(ord(crossword[r][s-inc])-32)
						inc+=1
					return True
def chec_vert_for(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r+inc][s]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r+inc][s])>96:
							crossword[r+inc][s]=chr(ord(crossword[r+inc][s])-32)
						inc+=1
					return True
def chec_vert_back(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r-inc][s]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r-inc][s])>96:
							crossword[r-inc][s]=chr(ord(crossword[r-inc][s])-32)
						inc+=1
					return True
def chec_diag1_back(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r-inc][s-inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r-inc][s-inc])>96:
							crossword[r-inc][s-inc]=chr(ord(crossword[r-inc][s-inc])-32)
						inc+=1
					return True
def chec_diag1_for(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r+inc][s+inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r+inc][s+inc])>96:
							crossword[r][s+inc]=chr(ord(crossword[r+inc][s+inc])-32)
						inc+=1
					return True
def chec_diag2_back(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r+inc][s-inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r+inc][s-inc])>96:
							crossword[r+inc][s-inc]=chr(ord(crossword[r+inc][s-inc])-32)
						inc+=1
					return True
def chec_diag2_for(word):
	for r in range(rows):
		for s in range(cols):
			inc=0
			cnt=0
			if crosswordx[r][s]==word[0]:
				try:
					while(inc<len(word) and(crosswordx[r-inc][s+inc]==word[inc])):
						inc+=1
						cnt+=1
				except IndexError:
					continue;
				if cnt==len(word):
					inc=0
					while(inc<cnt):
						if ord(crossword[r-inc][s+inc])>96:
							crossword[r-inc][s+inc]=chr(ord(crossword[r-inc][s+inc])-32)
						inc+=1
					return True


#randomly selecting the first player to play

turn=random.randint(0,int(player_cnt)-1)
words_guessed=0
guessed_words=[]
win = False

#game loop starts

while not win:
	word = input("\nPlayer " + str(turn) + ", please enter a word: ").strip()
	mark=0
	
	if word in line1[2:]:
		#calling functions one by one to find word.
		if not (word in guessed_words):	
			if mark==0 and chec_hori_for(word):
				mark=1
			elif mark==0 and chec_hori_back(word):
				mark=1
			elif mark==0 and chec_vert_for(word):
				mark=1
			elif mark==0 and chec_vert_back(word):
				mark=1
			elif mark==0 and chec_diag1_back(word):
				mark=1
			elif mark==0 and chec_diag1_for(word):
				mark=1
			elif mark==0 and chec_diag2_for(word):
				mark=1
			elif mark==0 and chec_diag2_back(word):
				mark=1
				
			words_guessed+=1
			guessed_words.append(word)
			if words_guessed==len(line1)-2:
				win=True
			
			store_list[turn].append(word)
			os.system("clear")
		
		else:
			os.system("clear")
			print("\nWord has been entered before")
		
	else:	
		os.system("clear")
		if len(word)<3 or word.isdigit() or (" " in word):
			print("\nInvalid input")
		else:
			print("\nWrong word!")

	#loop to print our updated crossword

	for j in range(rows):
		print("+"+"---+"*rows)
		print("|",end=" ")
		for k in range(cols):
				print(crossword[j][k]+" |", end=" ")
		print()

	print("+"+"---+"*rows)

	#printing the score after every turn and switching the turn

	print("\nScore:")
	for playerx in range(int(player_cnt)):
		print("Player",str(playerx)+':',str(len(store_list[playerx])),str(store_list[playerx]))

	turn = (turn + 1) % int(player_cnt)

print("\nGame Over!!")




