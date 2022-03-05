class ExchangeLossComparison:

    def __init__(self, dollar_amount, current_exchange_rate, former_exchange_rate):
        self._dollar_amount =dollar_amount
        self._current_exchange_rate = current_exchange_rate
        self._former_exchange_rate = former_exchange_rate

    def comparison(self):
        way1 = self.way1(self._dollar_amount, self._former_exchange_rate, self._current_exchange_rate)
        way2 = self.way2(self._dollar_amount, self._former_exchange_rate, self._current_exchange_rate)
        print('{} vs {}'.format(way1, way2))

    def way1(self, dollar_amount, selling_ex_rate, buying_ex_rate):
        won_amount = self.exchange_in_shinhan_investment(dollar_amount, selling_ex_rate)
        dollar_cash_amount = self.exchange_in_shinhan_bank(won_amount, buying_ex_rate, True)
        return dollar_cash_amount

    def way2(self, dollar_amount, selling_ex_rate, buying_ex_rate):
        return self.withdraw_cash_in_shinhan_bank(dollar_amount, buying_ex_rate)

    def exchange_in_shinhan_investment(self, amount, exchange_rate, buy_flag=False):
        original_exchange_fee_rate = 0.01   # 2022.02.28 신한금융투자 상담으로 확인함
        my_discount_rate = 0.95             # 2022.02.28 신한금융투자 상담으로 확인함
        actual_exchange_fee_rate = original_exchange_fee_rate * my_discount_rate

        if buy_flag:
            actual_exchange_rate = pow(exchange_rate * (1+actual_exchange_fee_rate), -1)
        else:
            actual_exchange_rate = exchange_rate * (1-actual_exchange_fee_rate)

        return amount * actual_exchange_rate

    def exchange_in_shinhan_bank(self, amount, exchange_rate, buy_flag=False):
        original_exchange_fee_rate = 0.0175   # 2022.02.28 신한은행 상담사 확인중
        my_discount_rate = 0.9              # SOL 편한 환전 공식 환전우대율
        actual_exchange_fee_rate = original_exchange_fee_rate * my_discount_rate

        if buy_flag:
            actual_exchange_rate = pow(exchange_rate * (1+actual_exchange_fee_rate), -1)
        else:
            actual_exchange_rate = exchange_rate * (1-actual_exchange_fee_rate)

        return amount * actual_exchange_rate

    def withdraw_cash_in_shinhan_bank(self, foreign_currency_amount, exchange_rate):
        withdraw_fee_rate = 0.015

        return foreign_currency_amount * (1-withdraw_fee_rate)


if __name__ == '__main__':
    total_dollar_amount = 1
    my_average_selling_exchange_rate = 1180
    final_exchange_rate = 1160

    e1 = ExchangeLossComparison(total_dollar_amount, final_exchange_rate, my_average_selling_exchange_rate)
    e1.comparison()

