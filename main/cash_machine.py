class CashMachine:

    def __init__(self):
        self.result = {}

    def cash_machine(self, requested_cash):
        try:
            if requested_cash % 10 > 0:
                return None
        except TypeError:
            return 'Informe um valor inteiro!'

        if requested_cash >= 100:
            return self.__split_cash(100, requested_cash)

        if requested_cash >= 50:
            return self.__split_cash(50, requested_cash)

        if requested_cash >= 20:
            return self.__split_cash(20, requested_cash)

        if requested_cash >= 10:
            return self.__split_cash(10, requested_cash)

    def __split_cash(self, note_value, request_value):
        number_notes = request_value // note_value
        self.result[note_value] = number_notes
        money_left = request_value - number_notes * note_value
        if money_left > 0:
            self.cash_machine(money_left)
        return self.result
