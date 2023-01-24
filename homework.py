class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, 
                 training_type: str, 
                 duration: float, 
                 distance: float, 
                 speed: float, 
                 calories: float) -> None:
        self.training_type =  training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        print(f'Тип тренировки: {self.training_type};'
              f'Длительность: {self.duration.f3} ч.;'
              f'Дистанция: {self.distance.f3} км;'
              f'Ср. скорость: {self.speed.f3} км/ч;'
              f'Потрачено ккал: {self.calories.f3}. ')             
        


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    """Длина шага или гребка в метрах"""
    M_IN_KM = 1000
    """Кол-во метров в километре"""



    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight         
    

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = self.get_distance() / self.duration        
        return mean_speed
        

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(training.__class__.__name__, 
                            self.duration, 
                            self.get_distance, 
                            self.get_mean_speed, 
                            self.get_spent_calories)


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

