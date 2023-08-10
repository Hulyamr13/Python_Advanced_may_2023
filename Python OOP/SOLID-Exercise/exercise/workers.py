class Workable:
    def work(self):
        pass


class Worker(Workable):
    def work(self):
        print("I'm working!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Workable), '`worker` must implement the Workable interface.'
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(Workable):
    def work(self):
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
