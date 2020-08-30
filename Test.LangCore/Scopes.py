

def set_global_var():
    ''' Объявление глобальной переменной внутри функции '''
    global z 
    z = 'Try set global value into function'


def set_scope_fun_var():
    ''' Изменение переменной внешней функции ее подфункцией '''
    car = 'Toyota'
    def set_name():
        nonlocal car
        car = "BMW"
        print("sub_function value:", car)
    set_name()
    print("function value: ", car)

set_global_var()
# Глобальная переменная стала доступна тут
print(z)

set_scope_fun_var()





