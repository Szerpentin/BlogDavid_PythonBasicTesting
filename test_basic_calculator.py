import basic_calculator

class Test_Handler:
    def test_sum_one(self):
        sum = basic_calculator.sum(2,3)
        assert sum == 5

    def test_sum_two(self):
        sum = basic_calculator.sum(66,55)
        assert sum == 121

class Test_My_Handler_Two:
    def test_sum_one(self):
        sum = basic_calculator.sum(2,3)
        assert sum == 5

    def test_sum_two(self):
        sum = basic_calculator.sum(66,55)
        assert sum == 121