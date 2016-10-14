
with open('./test.txt', 'r') as f:
	lines = f.readlines()

t = [e.strip() for e in lines]
print t

tt = [l.strip() for l in open('./test.txt', 'r')]
print tt

a = [1,2,3,4]
print map(lambda i: 2*i, a)

def input_arg1(a, *args):
	print("Print out args: %s"% a)
	for i in args: 
		print i
input_arg1('input1', 'input2', 'input3', 'input4')


def input_arg2(a, **args):
	print("Print out args: %s"% a)
	for i in args: 
		print "key: ", i, ", Value: ", args[i]

input_arg2('first arg', gang='charles', nan='cindy')

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3)
test_var_args_call(1, *args)


def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
