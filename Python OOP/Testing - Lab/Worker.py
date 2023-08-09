import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def test_initialization(self):
        worker = Worker("John", 1000, 10)
        self.assertEqual(worker.name, "John")
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_energy_increment(self):
        worker = Worker("John", 1000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_negative_energy_exception(self):
        worker = Worker("John", 1000, 0)
        with self.assertRaises(Exception):
            worker.work()

    def test_zero_energy_exception(self):
        worker = Worker("John", 1000, 0)
        with self.assertRaises(Exception):
            worker.work()

    def test_salary_increment(self):
        worker = Worker("John", 1000, 10)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_energy_decrement(self):
        worker = Worker("John", 1000, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker("John", 1000, 10)
        info = worker.get_info()
        self.assertEqual(info, "John has saved 0 money.")


if __name__ == '__main__':
    unittest.main()
