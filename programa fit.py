def img(sexo, idade, valorimc):
    if(sexo == 'masculino'):
        aux3 = (1.2 * valorimc) - 10.8 + (0.23 * float(idade)) - \
            5.4 * 1000.1/(25.5 * 25.5)
    elif(sexo == 'feminino'):
        aux3 = (1.2 * valorimc) + (0.23 * float(idade)) - \
            5.4 * 1000.1/(25.5 * 25.5)
    return round(aux3, 2)


def imc(peso, altura):
    aux = float(peso)/((float(altura)/100)*((float(altura)/100)))
    return round(aux, 2)


def calorias(sexo, idade, altura, peso):
    if(sexo == 'masculino'):
        aux2 = (13.75*float(peso))+(5*float(altura))-(6.76*float(idade))+66.5
    elif(sexo == 'feminino'):
        aux2 = (9.56*float(peso))+(1.85*float(altura))-(4.68*float(idade))+665
    return round(aux2, 2)


def start():
    altura = 0
    peso = 0
    valorimc = 0
    sexo = 0
    idade = 0
    valorimc = 0
    print('Ola! Bem-vindo a calculador FIT M&A')
    name = input('Qual o seu nome? ')
    print('Oi ' + name)
    while(True):
        print('Voce quer fazer o que?')
        print('Aqui nos fazemos calculo de imc, calculo de calorias diarias, fazemos uma lista de comidas saudaveis, porcentagem de gordura corporal.')
        escolha = input().lower()
        if('imc' in escolha):
            if(altura == 0 and peso == 0):
                altura = input('Qual a sua altura em centimetros? ')
                peso = input('Qual o seu peso em kg? ')
            valorimc = imc(peso, altura)
            print('O seu IMC é: ' + str(valorimc))
            if(valorimc < 16):
                print('Sua situação é: Subpeso Severo')
            elif(valorimc < 20):
                print('Sua situação é: Subpeso')
            elif(valorimc < 25):
                print('Sua situação é: Normal')
            elif(valorimc < 30):
                print('Sua situação é: Sobrepeso')
            elif(valorimc < 40):
                print('Sua situação é: Obeso')
            elif(valorimc > 40):
                print('Sua situação é: Obeso Morbido')
        elif('caloria' in escolha):
            if(altura == 0 and peso == 0):
                altura = input('Qual a sua altura em centimetros? ')
                peso = input('Qual o seu peso em kg? ')
            if(sexo == 0 and idade == 0):
                sexo = input(
                    'Qual o seu sexo?(masculino ou feminino) ').lower()
                idade = input('Qual a sua idade? ')
            valorcalorias = calorias(sexo, idade, altura, peso)
            print('Voce precisa consumir pelo menos: ' +
                  str(valorcalorias) + ' por dia')
        elif('comida' in escolha):
            print('Essas sao umas das comidas mais saudaveis do mundo!')
            print('1 -Salmao')
            print('2 -Ovo')
            print('3 -Aspargos')
            print('4 -Verduras de folha verde')
            print('5 -Amendoas')
            print('6 -Abacate')
            print('7 -Maça')
            print('8 -Tomate')
            print('9 -Azeite de Oliva')
            print('10 -Mel')
        elif('gordura' in escolha):
            if(sexo == 0 and idade == 0):
                sexo = input(
                    'Qual o seu sexo?(masculino ou feminino) ').lower()
                idade = input('Qual a sua idade? ')
            if(valorimc == 0):
                if(peso == 0 and altura == 0):
                    altura = input('Qual a sua altura em centimetros? ')
                    peso = input('Qual o seu peso em kg? ')
                valorimc = imc(peso, altura)
            valorimg = img(sexo, idade, valorimc)
            print('O sua taxa de gordura coporal é: ' + str(valorimg) + '%')


if __name__ == '__main__':
    start()
