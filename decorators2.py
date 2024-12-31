def brother(arg):
    def inner():
         print('brother start monitaring the sister')
         arg()
         print('brother end monitaring the sister')
    return inner


@brother
def sister():
    print('sister start speaking')
    print('sister ended speaking')

sister()    
