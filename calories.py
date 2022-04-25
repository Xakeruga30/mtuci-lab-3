from main import CaloriesCalculator
from main import Record


def test_get_calories_remained():
    cal = CaloriesCalculator(400)
    cal.add_record(Record(100, 'пирог'))
    cal.add_record(Record(300, 'яблоко'))
    res = cal.get_calories_remained()
    assert res == 50.0
