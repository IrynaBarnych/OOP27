# Завдання 4
# Створіть клас "Комп'ютер", який має зберігати інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін.

class Comp:
    def __init__(self, processor, OZY, videocard):
        self.processor = processor

    def OZY(self, OZY):
        self._OZY = OZY

    def videocarde(self, videocard):
        self._videocard = videocard




