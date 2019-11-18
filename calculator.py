def add(a,b) :
	return a+b

def multiply(a,b):
    try:
        x = a*b
    except ValueError:
        print ("Cannot multiply valid number")
        x = False
    return x
