from splits import settle_up

def test_two_creditors():
    assert settle_up({"A": 50, "B": 30, "C": -60, "D": -20}) == [('C', 'A', 50), ('D', 'B', 20), ('C', 'B', 10)]