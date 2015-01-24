def incrementcount():
	f = open('count.txt.', 'r+')
	#open file for reading, writing
	if not f:
		sleep(1)
		f = open('count.txt', 'r+')
		if not f:
			print("error!")
			return -1
	i = int(f.read(1))
	#get int i from file
	i += 1
	#increment i
	f.seek(0)
	f.write(str(i))
	#write i to file
	return i


def main():
	print("Content-type: text/html\n\n")
	print("<html><body><h1>The current count is: ", incrementcount())
	print("</h1></body></html>\n")