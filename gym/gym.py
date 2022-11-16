from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [cust for cust in self.customers if cust.id == subscription.customer_id][0]
        trainer = [tr for tr in self.trainers if tr.id == subscription.trainer_id][0]
        plan = [plan for plan in self.plans if plan.id == subscription.exercise_id][0]
        equipment = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
