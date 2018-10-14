from main.cash_machine import CashMachine


def Main():
    print('O ATM contem notas de 10, 20, 50 e 100 reais.')

    while True:
        try:
            requested_cash = int(input('Informe o valor do seu saque: '))
            result = atm(requested_cash)
            if result is None:
                print('Solicitação não atendida. A máquina trabalha apenas com notas de 10, 20, 50 e 100.')
            else:
                print('Valor do Saque: R$ {},00 – Resultado Esperado: {}.'.format(requested_cash, result))
        except ValueError:
            print('Informe um valor inteiro!')
            continue
        finally:
            exit = input('Você deseja sair? (s) sim ou (n) não. ')
            if exit.lower() == 's':
                break


def atm(requested_cash):
    if requested_cash == 0:
        return None
    atm = CashMachine()
    money = atm.cash_machine(requested_cash)
    if money is None or money == 0:
        return None
    result = 'Entregar'
    for note_value, number_notes in money.items():
        result += ' {} nota(s) de R${},00'.format(number_notes, note_value)
    return result


if __name__ == "__main__":
    Main()
