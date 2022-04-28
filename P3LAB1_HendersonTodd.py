# CTI-110
# P3LAB1
# Todd Henderson
# 29 April 2022

rgb = []

colr = []

for i in range(0,3):
	
     inp = int(input("Input: "))
	
     if (inp >=0 and inp<=255):
		
           rgb.append(inp)
		
     else:
		
           print("Range is 0 to 255")
		
           exit()
		
colr.extend(rgb)

rgb.sort()

for i in range(0,3):
	
     print(colr[i] - rgb[0])
