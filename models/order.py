class Order:
    def __init__(self, input_customer_name, input_order_date, input_quantity, input_product, input_product_price):
        self.customer_name = input_customer_name
        self.order_date = input_order_date
        self.quantity = input_quantity
        self.product = input_product
        self.product_price = input_product_price
        self._total_amount = 0

    def get_total_amount(self):
        self._total_amount += self.quantity * self.product_price
        return self._total_amount

