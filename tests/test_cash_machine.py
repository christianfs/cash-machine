from context import main
from unittest import TestCase
from main.cash_machine import CashMachine


class TestCashMachine(TestCase):
    def test_return_error_message(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine('w')
        assert cash == 'Informe um valor inteiro!'

    def test_return_10(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(10)
        assert cash == {10: 1}

    def test_return_20(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(20)
        assert cash == {20: 1}

    def test_return_30(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(30)
        assert cash == {10: 1, 20: 1}

    def test_return_40(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(40)
        assert cash == {20: 2}

    def test_return_50(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(50)
        assert cash == {50: 1}

    def test_return_60(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(60)
        assert cash == {10: 1, 50: 1}

    def test_return_70(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(70)
        assert cash == {50: 1, 20: 1}

    def test_return_80(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(80)
        assert cash == {50: 1, 20: 1, 10: 1}

    def test_return_90(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(90)
        assert cash == {50: 1, 20: 2}

    def test_return_100(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(100)
        assert cash == {100: 1}

    def test_return_120(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(120)
        assert cash == {100: 1, 20: 1}

    def test_return_130(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(130)
        assert cash == {100: 1, 20: 1, 10: 1}

    def test_return_150(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(150)
        assert cash == {100: 1, 50: 1}

    def test_return_180(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(180)
        assert cash == {100: 1, 50: 1, 20: 1, 10: 1}

    def test_return_390(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(390)
        assert cash == {100: 3, 50: 1, 20: 2}

    def test_return_1000(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(1000)
        assert cash == {100: 10}

    def test_return_1760(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(1760)
        assert cash == {100: 17, 50: 1, 10: 1}

    def test_return_13670(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(13670)
        assert cash == {100: 136, 50: 1, 20: 1}

    def test_return_13671(self):
        cash_machine = CashMachine()
        cash = cash_machine.cash_machine(13671)
        assert cash is None
