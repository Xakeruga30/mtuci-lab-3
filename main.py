import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if record.date == self.today:
                sum+=record.amount
        return sum

    def get_week_stats(self):
        sum = 0
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                sum += record.amount
        return sum
    def get_today_balance(self):
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.get_today_balance()
        if calories_remained > 0:
            print(f'Калорийность не превышена '
                       f'Но не более {calories_remained} кКал')
        else:
            print('Превышена норма калорий!')



class CashCalculator(Calculator):
    USD_RATE = 65.0
    EURO_RATE = 70.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('Rub', CashCalculator.RUB_RATE)}
        cash_remained = self.get_today_balance()
        if cash_remained == 0:
            return 'Денег нет!'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается!'
        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'Остаток: {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет! Долг: - {cash_remained} '
                       f'{name}')
        return message



class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()




















