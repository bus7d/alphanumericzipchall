#!/usr/bin/python2
#challenge Brut3M3
alphanum="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
past=["v","p","r","y"]
word=["vlvffw","ywfCgyf'gC","vddueDw","fb"]
y=0

def forge():
		global past,word,y,passw,wordz
	#while y<4:
		passw=past[y]
		wordz=word[y]
#		print "Counter:",y
#		print "Forged:",passw,wordz
		y=y+1
def tinker():
	global passw,wordz,alphanum
	x=0	
	if y==4:
		while x<len(alphanum):
					password=passw+wordz+alphanum[x]
					x=x+1
					print password


	if y<3:
		while x<len(alphanum):
			password=passw+alphanum[x]+wordz
			x=x+1
			print password
def main():
	global y
	while y<4:
		forge()
		tinker()

main()
