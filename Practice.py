def one(input1, input2):
	if len(input1) == len(input2):
		return input1 + " " + input2
       
	else:
		return max(input1, input2)
            


one("dad", "hello")