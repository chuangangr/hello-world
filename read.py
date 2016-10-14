
with open('./test.txt', 'r') as f:
	lines = f.readlines()

t = [e.strip() for e in lines]
print t


tt = [l.strip() for l in open('./test.txt', 'r')]
print tt

a = [1,2,3,4]
print map(lambda i: 2*i, a)
print filter(lambda i: i > 2, a)

def input_arg1(a, *args):
	print("Print out args: %s"% a)
	for i in args: 
		print i

input_arg1('input1', 'input2', 'input3', 'input4')



def input_arg2(a, **args):
	print("Print out args: %s"% a)
	for i in args: 
		print "key: ", i, ", Value: ", args[i] 


input_arg2('input1', baba='input2', mama='input3')
