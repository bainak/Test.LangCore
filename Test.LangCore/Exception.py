import os

def file_read():
	''' Читает файл без обработки исключение '''
	file = open('..\TestData\MT1001.txt', 'r')
	for line in file:
		print(line)

def file_read_1():
	''' Читает файл с общей обработкой исключение без возможности получить информацию об ошибке '''
	try:
		file = open('..\TestData\MT1001.txt', 'r')
		for line in file:
			print(line)
		print(f'File status before close: {file.closed}')
		file.close()
		print(f'File status after close: {file.closed}')
	except:
		print('Error happened, without info')

def file_read_2():
	''' Читает файл с общей обработкой исключение '''
	try:
		file = open('..\TestData\MT1001.txt', 'r')
		for line in file:
			print(line)
		file.close()
	except Exception as e:
		print('Had info about error.')
		print(e)



def file_read_3():
	''' Читает файл с группой типов исключений '''
	try:
		file = open('..\TestData\MT1001.txt', 'r')
		for line in file:
			print(line)
		file.close()
	except (PermissionError, FileNotFoundError) as e:
		print(e)

def file_read_4():
	''' Читает файл с индивидуйльной обработка каждого типа исключение '''
	try:
		file = open('..\TestData\MT1001.txt', 'r')
		for line in file:
			print(line)
		file.close()
	except PermissionError as e:
		print(e)
	except FileNotFoundError as e:
		print(e)
	except Exception as e:
		print(e)

def file_read_5():
	''' Читает файл с индивидуaльной обработка каждого типа исключение
        и дополнительнными операторами else, finally '''
	try:
		file_name = '..\TestData\MT100.txt'
		file = open(file_name, 'a+')
		for line in file:
			print(line)

		# Writing to file.
		for i in range(1, 10):
			file.write(f'Added new row: {i}\n')
	except PermissionError as e:
		print(e)
	except FileNotFoundError as e:
		print(e)
	except Exception as e:
		print(e)
	else:
		print('File exist, error doesn\'t happened.')
	finally:
		if file != None:
			file.close()
			print('The file was closed.')
		else:
			print('The file wasn\'t opened.')

def file_read_6():
	''' Проверяет на наличие существование файла, если его нет генирируем исключение, принудительно '''
	try:
		fname = '..\TestData\MT100.txt'
		if not os.path.isfile(fname):
			raise FileNotFoundError('This is custom file exception:', {'param': fname, 'method': 'file_read_6'})
		else:
			file = open(fname, 'r')
			for line in file:
				print(line)
			file.close()
	except FileNotFoundError as e:
		print(e)
	except Exception as e:
		print(e)

def file_read_7():
	''' Обеспечение бызопасного освобождение ресурсов с помощью оператора with '''
	try:
		
		fname = '..\TestData\MT100.txt'
		with open(fname, 'r') as file:
			for line in file:
				print(line)
			print(f'File status in with area: {file.closed}')
		print(f'File status after with area: {file.closed}')
	except FileNotFoundError as e:
		print(e)
	except Exception as e:
		print(e)


file_read_7()