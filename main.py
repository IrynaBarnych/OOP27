# Завдання 4
# Створіть клас "Комп'ютер", який має зберігати інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін.

class Computer:
    def __init__(self, processor, OZY, videocard):
        self._processor = processor
        self._OZY = OZY
        self._videocard = videocard

    def get_processor(self):
        return self._processor

    def get_OZY(self):
        return self._OZY

    def set_OZY(self, value):
        self._OZY = value

    def get_videocard(self):
        return self._videocard

    def set_videocard(self, value):
        self._videocard = value


computer = Computer("Intel i7", "16GB", "NVIDIA GeForce GTX 1080")
print(f"Процесор: {computer.get_processor()}")
print(f"ОЗУ: {computer.get_OZY()}")
print(f"Відеокарта: {computer.get_videocard()}")

computer.set_OZY("32GB")
computer.set_videocard("NVIDIA GeForce RTX 3070")

print(f"Оновлені дані: {computer.get_processor()}, {computer.get_OZY()}, {computer.get_videocard()}")






