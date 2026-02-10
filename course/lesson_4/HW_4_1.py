from excel_manager import ReadExcelFile

# =====================================
# Primitive Store Management System
# =====================================


# -------- Product class --------
class Product:
    def __init__(
        self, product_name: str, category: str, price: float, quantity_in_stock: int
    ) -> None:
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def change_price(self, new_price: float) -> None:
        self.price = new_price

    def change_quantity(self, qty: int) -> None:
        self.quantity_in_stock = qty


# -------- Order class --------
class Order:
    def __init__(self) -> None:
        self.products_list: list = []  # list of (Product, quantity)
        self.total_amount: float = 0.0

    def add_product(self, quantity_in_stock: Product, new_order: list) -> None:

        qty: int = new_order[3]
        if qty == 0:
            error_msg = f"❌ Cannot order {qty}s. Quantity must be greater than 0."
            self.products_list.append(error_msg)
            return
        if isinstance(qty, int):
            if quantity_in_stock.quantity_in_stock < qty:
                error_msg = f"❌ Only {quantity_in_stock.quantity_in_stock}(s) '{quantity_in_stock.product_name}' available. You requested {qty}."
                self.products_list.append(error_msg)
                return
        if isinstance(qty, int):
            self.products_list.append(new_order)
            quantity_in_stock.quantity_in_stock -= qty
            self.calculate_total()

    def calculate_total(self) -> None:

        self.total_amount: int = 0
        for item in self.products_list:
            self.total_amount += item[2] * item[3]


# -------- Customer class --------
class Customer:
    def __init__(self, customer_name: str, customer_email: str) -> None:
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.orders_list: list = []

    def add_order(self, customer_order: list) -> None:
        self.orders_list.append(customer_order)
        # print(self.customer_name, customer_order)
        self.display_info()

    def display_info(self) -> None:

        print(f"\n👤 Customer: {self.customer_name}")
        print(f"   Email: {self.customer_email}")

        if self.orders_list:
            print("   📋 Orders:")
            total_customer: int = 0
            for order_group in self.orders_list:
                if isinstance(order_group, list):
                    for item in order_group:
                        if isinstance(item, list) and len(item) >= 4:
                            product_total = item[2] * item[3]
                            total_customer += product_total
                            print(
                                f"      • {item[0]} {item[3]} x ${item[2]} = ${product_total:.2f}"
                            )
                        elif isinstance(item, str):
                            print(f"      • {item}")
            print(f"   💰 Total: ${total_customer:.2f}")
        else:
            print("   No orders yet")


def initial_store_state(quantity_in_stock_list: list) -> None:
    print("\n" + "=" * 50)
    print("\nINITIAL STORE STATE")
    print("=" * 50)

    initial_state_lines = [
        f"{product_name} | {category} | Price: {price} | Stock: {quantity_in_stock}"
        for product_name, category, price, quantity_in_stock in quantity_in_stock_list
    ]
    print("\n".join(initial_state_lines))

    print("=" * 50)


def order_details(customer_order_list: list) -> None:

    print("\n" + "=" * 50)
    print("\nORDER DETAILS")
    print("=" * 50)

    for product_name, category, price, quantity in [
        item for _, item in customer_order_list
    ]:

        item_total = price * quantity
        print(f"{product_name} x {quantity} = {item_total:.2f}")

    # Calcular total con sum()
    total_general = sum(
        price * quantity for _, (_, _, price, quantity) in customer_order_list
    )
    print(f"Total order amount: ${total_general:.2f}")


def final_store_state(products_inventory) -> None:

    print("\n" + "=" * 50)
    print("\nFINAL STORE STATE")
    print("=" * 50)

    for product in products_inventory:
        print(
            f"{product.product_name} | {product.category} | "
            f"Price: ${product.price:.2f} | Stock: {product.quantity_in_stock}"
        )


# =====================================
# Task 2: Interaction between classes
# (Simulated initial store state)
# =====================================


class CreateOrder:

    # Initial products (as if read from file)
    @staticmethod
    def create_orders() -> None:

        quantity_in_stock_list, customer_order_list = (
            ReadExcelFile.read_all_from_excel()
        )
        initial_store_state(quantity_in_stock_list=quantity_in_stock_list)

        products_inventory: list[Product] = [
            Product(product_name=name, category=cat, price=price, quantity_in_stock=qty)
            for name, cat, price, qty in quantity_in_stock_list
        ]
        for products, (customer, order_list) in zip(
            products_inventory, customer_order_list
        ):

            order: Order = Order()
            order.add_product(quantity_in_stock=products, new_order=order_list)
            customers: Customer = Customer(
                customer_name=customer[0], customer_email=customer[1]
            )
            customers.add_order(customer_order=order.products_list)

        order_details(customer_order_list=customer_order_list)
        final_store_state(products_inventory=products_inventory)


CreateOrder().create_orders()
