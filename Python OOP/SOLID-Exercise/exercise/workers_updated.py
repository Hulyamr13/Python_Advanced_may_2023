from abc import ABCMeta, abstractmethod
import time


class Workable(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass


class Eatable(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must implement the Workable interface."
        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        if isinstance(self.worker, Eatable):
            self.worker.eat()

class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


work_manager = Manager()
break_manager = Manager()

work_manager.set_worker(Worker())
break_manager.set_worker(Worker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
work_manager.lunch_break()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
