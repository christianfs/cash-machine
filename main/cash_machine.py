class CashMachine:

    def __init__(self):
        self.result = {}

    def cash_machine(self, requested_cash):
        if requested_cash % 10 > 0:
            return 'Solicitação não atendida. A máquina trabalha apenas com notas de 10, 20, 50 e 100.'

        if requested_cash >= 100:
            return self.__split_cash(100, requested_cash)

        if requested_cash >= 50:
            return self.__split_cash(50, requested_cash)

        if requested_cash >= 20:
            return self.__split_cash(20, requested_cash)

        if requested_cash >= 10:
            return self.__split_cash(10, requested_cash)

    def __split_cash(self, value, request):
        money_notes = request // value
        self.result[value] = money_notes
        money_left = request - money_notes * value
        if money_left > 0:
            self.cash_machine(money_left)
        return self.result
