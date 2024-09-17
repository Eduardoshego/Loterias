from os import system as sys

def executa_aplicacao(aplication_name):
    sys(f'flet run {aplication_name}.py -w')
    
if __name__ == '__main__':
    executa_aplicacao('index')