class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        customer = self.get_customer(subscription.customer_id)
        trainer = self.get_trainer(subscription.trainer_id)
        equipment = self.get_equipment(subscription.exercise_id)
        plan = self.get_plan(subscription.exercise_id)
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

    def get_subscription(self, subscription_id):
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                return subscription

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def get_trainer(self, trainer_id):
        for trainer in self.trainers:
            if trainer.id == trainer_id:
                return trainer

    def get_equipment(self, equipment_id):
        for equipment in self.equipment:
            if equipment.id == equipment_id:
                return equipment

    def get_plan(self, exercise_id):
        for plan in self.plans:
            if plan.id == exercise_id:
                return plan
