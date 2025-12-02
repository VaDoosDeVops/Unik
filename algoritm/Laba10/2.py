class Menu:
    def __init__(self):
        self.items = {
            "пеперони": 450,
            "четыре сыра": 500,
            "суприм": 550,
            "вегетарианская": 400
        }

    def is_available(self, pizza_name):
        return pizza_name.strip().lower() in self.items

    def get_price(self, pizza_name):
        return self.items[pizza_name.strip().lower()]


class OrderProcessor:
    def __init__(self, menu):
        self.menu = menu

    def process_orders(self, pizza_list):
        total = 0
        receipt = "Ваш заказ:\n"

        # Используем while вместо for для обхода списка пицц
        idx = 0
        while idx < len(pizza_list):
            pizza = pizza_list[idx].strip().lower()
            if self.menu.is_available(pizza):
                price = self.menu.get_price(pizza)
                total += price
                receipt += f"  {pizza} — {price} руб.\n"
            else:
                receipt += f"  {pizza} — нет в меню\n"
            idx += 1  # явное увеличение индекса

        receipt += f"Итого: {total} руб."
        return receipt


class PizzaOrderApp:
    def __init__(self):
        self.menu = Menu()
        self.processor = OrderProcessor(self.menu)

    def run(self):
        print("Добро пожаловать в пиццерию!")
        print("Доступные пиццы: пеперони, четыре сыра, суприм, вегетарианская")
        user_input = input("Введите названия пицц через запятую: ")

        pizza_list = user_input.split(",")
        receipt = self.processor.process_orders(pizza_list)

        print(receipt)


# Запуск приложения
if __name__ == "__main__":
    app = PizzaOrderApp()
    app.run()
