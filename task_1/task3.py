import numpy as np
import matplotlib.pyplot as plt

# Фиксированные значения
freq = 2 * np.pi * 1.0 # Частота синусоиды (1 Гц)
init_phase = 0 # Начальная фаза
amp = 1.0 # Амплитуда

# Создаем массив значений по синусоидальному законам
t = np.linspace(0, 2 * np.pi, 1000) # Создаем массив времени
sin_array = amp * np.sin(freq * t + init_phase)
cos_array = amp * np.cos(freq * t + init_phase)

# Создаем первый график для синусоиды
plt.figure(figsize=(12, 6)) # Увеличиваем размер графика
plt.subplot(1, 2, 1) # Создаем первый subplot
plt.plot(t, sin_array, label='A * sin(w*t)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('Синусоида')
plt.legend()

# Создаем второй график для косинусоиды
plt.subplot(1, 2, 2) # Создаем второй subplot
plt.plot(t, cos_array, label='A * cos(w*t)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('Косинусоида')
plt.legend()

# Отображаем графики
plt.tight_layout() # Для более компактного размещения графиков
plt.show()
