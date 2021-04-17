def rotate(arg1, arg2, arg3):
	"""
	Function receives three arguments and returns a tuple 
    in which the first argument is at index 1, 
    the second argument is at index 2 and the third argument is at index 0
	"""
	return arg3, arg1, arg2


a, b, c = "Doug", 22, 1984
print(f"{'Initial values are':<35} a: {a:<5} b: {b:<5} c: {c:<5}")

a, b, c = rotate(a, b, c)
print(f"{'Values after first rotation are':<35} a: {a:<5} b: {b:<5} c: {c:<5}")

a, b, c = rotate(a, b, c)
print(f"{'Values after second rotation are':<35} a: {a:<5} b: {b:<5} c: {c:<5}")

a, b, c = rotate(a, b, c)
print(f"{'Values after third rotation are':<35} a: {a:<5} b: {b:<5} c: {c:<5}")
