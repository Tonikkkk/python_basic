import doctest

class Car:
    def __init__(self, brand: str, max_speed: float):
        """
        Создание объекта "Автомобиль".

        :param brand: Бренд автомобиля
        :param max_speed: Максимальная скорость автомобиля в км/ч

        Примеры:
        >>> car = Car("Toyota", 200)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("max_speed должен быть положительным числом")
        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, increase: float) -> None:
        """
        Увеличить скорость автомобиля.

        :param increase: Величина увеличения скорости в км/ч

        Примеры:
        >>> car = Car("Toyota", 200)
        >>> car.accelerate(50)
        """
        if not isinstance(increase, (int, float)) or increase <= 0:
            raise ValueError("increase должен быть положительным числом")
        self.current_speed = min(self.current_speed + increase, self.max_speed)

    def brake(self, decrease: float) -> None:
        """
        Уменьшить скорость автомобиля.

        :param decrease: Величина уменьшения скорости в км/ч

        Примеры:
        >>> car = Car("Toyota", 200)
        >>> car.brake(30)
        """
        if not isinstance(decrease, (int, float)) or decrease <= 0:
            raise ValueError("decrease должен быть положительным числом")
        self.current_speed = max(self.current_speed - decrease, 0)

class Smartphone:
    def __init__(self, brand: str, battery_capacity: int):
        """
        Создание объекта "Смартфон".

        :param brand: Бренд смартфона
        :param battery_capacity: Емкость батареи в мАч

        Примеры:
        >>> phone = Smartphone("Samsung", 5000)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("battery_capacity должен быть положительным целым числом")
        self.brand = brand
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def charge(self, amount: int) -> None:
        """
        Зарядить смартфон.

        :param amount: Величина заряда в процентах

        Примеры:
        >>> phone = Smartphone("Samsung", 5000)
        >>> phone.charge(20)
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("amount должен быть положительным целым числом")
        self.battery_level = min(self.battery_level + amount, 100)

    def use(self, amount: int) -> None:
        """
        Использовать заряд батареи.

        :param amount: Величина расхода заряда в процентах

        Примеры:
        >>> phone = Smartphone("Samsung", 5000)
        >>> phone.use(30)
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("amount должен быть положительным целым числом")
        if amount > self.battery_level:
            raise ValueError("Недостаточно заряда")
        self.battery_level -= amount

class Backpack:
    def __init__(self, brand: str, capacity: float):
        """
        Создание объекта "Рюкзак".

        :param brand: Бренд рюкзака
        :param capacity: Вместимость рюкзака в литрах

        Примеры:
        >>> backpack = Backpack("Nike", 25)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("capacity должен быть положительным числом")
        self.brand = brand
        self.capacity = capacity
        self.current_load = 0

    def add_item(self, volume: float) -> None:
        """
        Добавить предмет в рюкзак.

        :param volume: Объем предмета в литрах

        Примеры:
        >>> backpack = Backpack("Nike", 25)
        >>> backpack.add_item(5)
        """
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("volume должен быть положительным числом")
        if self.current_load + volume > self.capacity:
            raise ValueError("Рюкзак переполнен")
        self.current_load += volume

    def remove_item(self, volume: float) -> None:
        """
        Удалить предмет из рюкзака.

        :param volume: Объем удаляемого предмета в литрах

        Примеры:
        >>> backpack = Backpack("Nike", 25)
        >>> backpack.remove_item(3)
        """
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("volume должен быть положительным числом")
        if volume > self.current_load:
            raise ValueError("Недостаточно места для удаления")
        self.current_load -= volume

if __name__ == "__main__":
    doctest.testmod()
