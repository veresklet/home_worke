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
        """Возвращает текстовую строку с информацией о тренировке."""    
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}. ')             


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    """Длина шага или гребка в метрах."""
    M_IN_KM: int = 1000
    """Коэффициент для перевода из метров в километры."""
    MIN_IN_H: int = 60
    """Коэффициент для перевода из минут в часы."""


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
        """Получить среднюю скорость движения км/ч."""
        mean_speed: float = self.get_distance() / self.duration        
        return mean_speed


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass


    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return  InfoMessage(self.__class__.__name__, 
                           self.duration, 
                           self.get_distance(), 
                           self.get_mean_speed(), 
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
    """Множитель средней скорости."""
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79
    """Сдвиг средней скорости."""


    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)


    def get_spent_calories(self) -> float:
        calories: float = (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER*self.get_mean_speed()
            +self.CALORIES_MEAN_SPEED_SHIFT)*self.weight
            /(self.M_IN_KM*self.duration/self.MIN_IN_H))
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    """Множитель веса спортсмена."""
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    """Множитель частного квадрата средней скорости и роста спортсмена."""
    KMH_IN_MSEC: float = 0.278
    """Коэффициент для перевода значений из км/ч в м/с."""
    CM_IN_M: int = 100
    """Коэффициент для перевода значений из сантиметров в метры."""

    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float, 
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories: float = ((
            self.CALORIES_WEIGHT_MULTIPLIER*self.weight+(self.get_mean_speed()*
            self.KMH_IN_MSEC**2/(self.height*self.CM_IN_M))*
            self.CALORIES_SPEED_HEIGHT_MULTIPLIER*self.weight)*
            self.duration*self.MIN_IN_H)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    """Длина гребка в метрах."""
    CALORIES_MEAN_SPEED_SHIFT = 1.1
    """Коэффициент для смещения значения средней скорости."""
    CALORIES_WEIGHT_MULTIPLIER = 2
    """Коэффициент для множителя скорости."""

    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float, 
                 lenght_pool: int, 
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения км/ч."""
        mean_speed: float = (self.lenght_pool*self.count_pool 
                            / self.M_IN_KM / self.duration)
        return mean_speed 


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((self.get_mean_speed()+self.CALORIES_MEAN_SPEED_SHIFT)
                    *self.CALORIES_WEIGHT_MULTIPLIER*self.weight*self.duration)
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_data: dict[str, type[Training]]={'SWM': Swimming,
                                             'RUN': Running,
                                             'WLK': SportsWalking}
    if workout_type in workout_data:
        return workout_data[workout_type](*data)
        


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    """Тестовые данные для имитации работы датчиков."""
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)