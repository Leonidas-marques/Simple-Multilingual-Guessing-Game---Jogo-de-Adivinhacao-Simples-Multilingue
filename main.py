from deep_translator import GoogleTranslator
from random import randint

languages_dict = GoogleTranslator.get_supported_languages(as_dict=True)

print('Supported languages:')
for key, value in languages_dict.items():
    print('type {value} to {key}'.format(value=value, key=key))

while True:
    language = str(input('Chosse your language: ')).strip()
    if language in languages_dict.values():
        break
    else:
        print('Choose a valid language, enter his abbreviation')

def translate(text):
    if language == 'pt':
        return text
    else:
        text = GoogleTranslator(source='pt', target=language).translate(text)
        return text

print(translate('Bem-vindo!\nAdivinhe o número secreto\n'))
while True:
    points = 1000
    secret_number = randint(1,100)
    won = False
    dificulty = int(input(translate('O número secreto entre 1 e 100!\nEscolha o modo de dificuldade!\n1-Modo Fácil\n2-Modo Médio\n3-Modo Difícil\nSua Escolha: ')))
    if dificulty in [1,2,3]:
        if dificulty == 1:
            guesses = 100
            point_value = 10
        elif dificulty == 2:
            guesses = 50
            point_value = 40
        elif dificulty == 3:
            guesses = 10
            point_value = 300
        else:
            continue
        while guesses > 0 :
            print(secret_number)
            print(translate('Você tem {} tentativas restantes'.format(guesses)))
            guess = int(input(translate('Adivinhe o número: ')))
            if guess > secret_number:
                print(translate('O número secreto é menor!'))
            elif guess < secret_number:
                print(translate('O número secreto é maior!'))
            elif guess == secret_number:
                print(translate('Você adivinhou corretamente!\nVocê ganhou!'))
                print(translate('Total de pontos: {}'.format(points))) 
                won = True
                break
            else:
                print(translate('Ocorreu algum erro...\nReiniciando...'))
                continue
            guesses -= 1
            points = guesses * point_value

        if guesses <= 0 or won:
            if not won:
                print(translate('Você Perdeu!'))
            keep_playing = str(input(translate('Deseja continuar jogando? (Y/N): '))).upper()
            if keep_playing == 'Y':
                continue
            elif keep_playing == 'N':
                break
            else:
                print(translate('Comando inválido!\nReiniciando...'))
                continue
        else:
            print(translate('Ocorreu algum erro...\nReiniciando...'))
            continue

    else:
        print(translate('Digite um número válido! (1,2,3)'))
        continue

print(translate('Obrigado por jogar!'))
    
