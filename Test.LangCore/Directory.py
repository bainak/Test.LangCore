import os

def get_all_dirs():
	''' Получение списка папок '''
	path = '..\TestData\Input'
	dirs = os.listdir(path)
	for dir in dirs:
		full_path = f'{path}\\{dir}'
		if os.path.isdir(full_path):
			print(f'Dir name is {dir}')
		elif os.path.isfile(full_path):
			print(f'File name is {dir}')
		else:
			print(f'Not clear type {dir}')


def make_dir():
	''' Создание папки '''
	path = '..\TestData\Input\\'
	dir_name = '20200828'
	try:
		full_path = f'{path}{dir_name}'	
		if not os.path.isfile(full_path):
			raise FileNotFoundError('The folder already exists:', {'param': full_path, 'method': 'make_dir'})
		else:
			os.mkdir(full_path)
	except FileExistsError as e:
		print(e)
	except Exception as e:
		print(e)



# make_dir()
get_all_dirs();
