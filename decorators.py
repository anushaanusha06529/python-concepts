def outer(arg):
    print('outer is started')
    print(arg)
    def inner():
        print('inner is started')
        arg()
        print('inner is ended')
    print('outer is ended')
    return inner

@outer

def hai():
    print('hai started')
    print('hai ended')
print(hai)
hai()
