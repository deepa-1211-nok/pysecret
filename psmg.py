def Registration():
	nrg = []
	print('タイトルを入力してください。')
	title = input()
	print('IDを入力してください。')
	ID = input()
	print('パスワードを入力してください')
	pw = input()
	print(title,ID,pw)
	list = [title,ID,pw]
	nrg.append(list)	

	return nrg




def main():
	foo = Registration() 
	print(foo)
	# print('Menu')
	# print('List(ls)')
	# print('Serch(sc)')
	# print('Registration(rg)')
	# print('change(cg)')

if __name__ == '__main__':
	main()



# if command = 'rg':
	# return Registration

	
