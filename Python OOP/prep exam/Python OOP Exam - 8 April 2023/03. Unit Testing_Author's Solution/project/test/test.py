import unittest
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.car = SecondHandCar('Toyota', 'Sedan', 50000, 20000)

    def test_initialization(self):
        self.assertEqual(self.car.model, 'Toyota')
        self.assertEqual(self.car.car_type, 'Sedan')
        self.assertEqual(self.car.mileage, 50000)
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])

    def test_set_promotional_price(self):
        self.car.set_promotional_price(18000)
        self.assertEqual(self.car.price, 18000)

        with self.assertRaises(ValueError):
            self.car.set_promotional_price(22000)

    def test_need_repair(self):
        self.car.need_repair(5000, 'Oil change')
        self.assertEqual(self.car.price, 25000)
        self.assertEqual(self.car.repairs, ['Oil change'])

        with self.assertRaises(ValueError):
            self.car.need_repair(15000, 'Engine repair')

    def test_comparison(self):
        other_car = SecondHandCar('Toyota', 'SUV', 60000, 18000)

        with self.assertRaises(TypeError):
            self.car > other_car

        self.assertEqual(self.car > self.car, False)

        other_car.car_type = 'Sedan'
        self.assertEqual(self.car > other_car, True)

    def test_price_mileage_constraints(self):
        with self.assertRaises(ValueError):
            SecondHandCar('Ford', 'Sedan', 50, 1)

        with self.assertRaises(ValueError):
            SecondHandCar('Ford', 'Sedan', 50, 20000)

    def test_str_method(self):
        expected_output = "Model Toyota | Type Sedan | Mileage 50000km\nCurrent price: 20000.00 | Number of Repairs: 0"
        self.assertEqual(str(self.car), expected_output)

        self.car.need_repair(5000, 'Oil change')
        expected_output_with_repairs = "Model Toyota | Type Sedan | Mileage 50000km\nCurrent price: 25000.00 | Number of Repairs: 1"
        self.assertEqual(str(self.car), expected_output_with_repairs)


if __name__ == '__main__':
    unittest.main()