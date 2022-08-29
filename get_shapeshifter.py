#!/usr/bin/python3

import wget

def checkInput (x):
		try:
			if len(x) == 3:
				int(x)
			else:
				print("\nYour number needs to be in the 3 digit format Jimmy can't you read ;)\n\nTRY AGAIN!!!!\n")
				return 1
		except:
			print("\nSilly Billy, that's not a number heehheheheheheeh........\n\nTRY AGAIN!!!!\n")
			return 1
		return 0

print("\n\nWARNING: If your page or chapter doesn't exist, nothing will be downloaded! Also make sure you are in the folder you want the downloads to go to!\n\n")

while True:
	x = str(input('From which page would you like to start? Keep in mind it will start 1 page after your selection. i.e. typing \'000\' will start on page \'001\' \n. \nAnd make sure it is in the format of a 3 digit number. \ni.e. Type \'000\' to start from the beginning or \'049\' to start from page 49.\n'))
	myCheck = checkInput(x)
	if myCheck == 0:
		break


part_number = input('Which part do you want? ;)\n')
part_url = 'http://lemonfontcomics.com/assets/comics/shapeshifter/part_' + part_number +  '/'

print("Don't be scared if it seems to stop. Just let it ride........\n\n\n\n\nHis site is slow af but I love 'em...\n")


while True:
	try:
		if x[0] == '0' and x[1] == '0' and int(x) != 9:
			z = int(x)
			z += 1
			x = '0' + '0' + str (z)
			wget.download(part_url + x + '.png')
		elif x[0] =='0' and int(x) != 99:
			z = int(x)
			z += 1
			x = '0' + str(z)
			wget.download(part_url + x + '.png')
		else:
			z = int(x)
			z += 1
			x = str(z)
			wget.download(part_url + x + '.png')

	except:
		print("\n\n\nIt starts with the coom and ends with cruel tears....\n\nEnjoy friends :\')")
		break



	
