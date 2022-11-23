from abc import ABC, abstractmethod
import time


# Creating a mixin class for workers
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


# Creating a mixin class for lunch breaks
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


# The worker can work And eat
class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


# The super worker can work faster and eat faster
class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


# The robot doesn't eat, it only works
class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):

    # Setting a worker
    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):

    # Setting a worker that is able to eat
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
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

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

