import json

def Registration():
	print('タイトルを入力してください。')
	title = input()
	print('IDを入力してください。')
	ID = input()
	print('パスワードを入力してください')
	pw = input()
	nrg = {title:{ID:pw}}	

	return nrg




def main():
	json_file = open('pass.json','r')
	json_object = json.load(json_file)
	print(json_object)
	
	foo = Registration()

	json_object.update(foo)
	print(json_object)
	json.dump(json_object,open('pass.json','w'))


	# print('Menu')
	# print('List(ls)')
	# print('Serch(sc)')
	# print('Registration(rg)')
	# print('change(cg)')

if __name__ == '__main__':
	main()



# if command = 'rg':
	# return Registration

	
