import json

# TODO:メソッド名は小文字で書いておくこと
# Inputで取ってきていたものは別のしごととして切り出す。
def Registration(title, ID, pw):
	# print('タイトルを入力してください。')
	# title = input()
	# print('IDを入力してください。')
	# ID = input()
	# print('パスワードを入力してください')
	# pw = input()
	return {title:{ID:pw}}


def main():
	json_file = open('pass.json','r')
	json_object = json.load(json_file)
	print(json_object)
	
	foo = Registration()

	json_object.update(foo)
	print(json_object)
	json.dump(json_object,open('pass.json','w'))


if __name__ == '__main__':
	main()



# if command = 'rg':
	# return Registration

	
