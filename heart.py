def printLove(start,length,midnumber=0,flag=31):
    for i in range(31):
        if i<start or i>start+length-1 and i<15-(midnumber-1)/2 or i>15+(midnumber-1)/2 and i<31-start-length or i> 30-start or i==flag:
            print(" "),
        else:
          print("*"),
    print("")
	for i in range(16):
		if i==0:
			printLove(4,3)
		elif i==1:
			printLove(1,9)
		elif i>=2 and i<=5:
			printLove(0,i+10)
		elif i==6:
			printLove(1,7,7,15)
		elif i>=7 and i<=8:
			printLove(i-5,6,5-(i-7)*2)
		elif i==9:
			printLove(5,6,1)
		elif i==10:
			printLove(8,6,1)
		elif i==15:
			printLove(15,1,1)
		else:
			printLove(i-1,16-i,1)
