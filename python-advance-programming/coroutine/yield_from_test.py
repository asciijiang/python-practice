from itertools import chain

my_list = [1,2,3]
my_dict = {
	"bobby1":"http://projectsedu.com",
	"bobby2":"http://www.imooc.com",
}

for value in chain( my_list,my_dict,range(5,10) ):
	print(value)