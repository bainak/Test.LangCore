import datetime

def FnDecore(fn):
    def FileFnDecore(fileContent):
        print('Before call fn')
        fn(fileContent)
        print('After call fn')
    return FileFnDecore

# function
@FnDecore
def WriteToFile(text):
    print('Start run WriteToFile')
    pathFile = 'E:\SourcesGit\python\Test\Lesson1\TestData\Files'
    pathFile = pathFile +'\\'+str(datetime.datetime.today().strftime('%Y-%m-%d-%H.%M.%S')) + '.txt'
    file = open(pathFile, 'a')
    file.write(text + '\n')
    file.close()
    return  file.name

WriteToFile('Try to decored a function')

# Декоратор на функцию
def decore_method(fn):

    def audit_make_log(msg):
        print('Run method: ' + str(fn.__name__))
        return fn(msg)
    return audit_make_log

#Основная функция
@decore_method
def make_log(msg):
    print(msg)
    if(len(msg) > 10):
        return True
    else:
        return False


fn = decore_method(make_log)
# fn('Hello World!')
make_log= fn
make_log('Hello world!')
