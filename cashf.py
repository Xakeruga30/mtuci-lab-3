from main import CashCalculator
from main import Record

def test_get_today_cash_remained():
    cash = CashCalculator(500)
    cash.add_record(Record(100, 'foot'))
    cash.add_record(Record(100, 'head'))
    print(cash.get_today_cash_remained("usd"))
    res = cash.get_today_cash_remained("usd")
    assert res == 4.15
