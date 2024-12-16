import numpy as np
import matplotlib.pyplot as plt
import os

#шлях до файлу
data_file = "C:/Users/LERA/Desktop/DS1.txt"

#перевірка наявності файлу
if not os.path.exists(data_file):
    print(f"Файл {data_file} не знайдено у поточній папці: {os.getcwd()}")
    exit()

#зчитування координат точок
points = []
with open(data_file, "r") as file:
    for line in file:
        x, y = map(int, line.strip().split())
        points.append((x, y))

x_coords, y_coords = zip(*points)

#параметри обертання
alpha = 20
alpha_rad = np.radians(alpha)
center = np.array([480, 480])

#афінне перетворення
cos_a, sin_a = np.cos(alpha_rad), np.sin(alpha_rad)
rotation_matrix = np.array([[cos_a, -sin_a],
                            [sin_a, cos_a]])

shifted_points = np.vstack((x_coords, y_coords)).T - center
rotated_points = shifted_points @ rotation_matrix.T
result_points = rotated_points + center

x_rot, y_rot = result_points[:, 0], result_points[:, 1]

#візуалізація результату
canvas_width, canvas_height = 960, 540
plt.figure(figsize=(canvas_width / 100, canvas_height / 100))
plt.plot(x_rot, y_rot, 'b.', label="Rotated Points")
plt.plot(x_coords, y_coords, 'r.', label="Original Points", alpha=0.5)

#налаштування системи координат
plt.xlim(0, canvas_width)
plt.ylim(0, canvas_height)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Афінне перетворення: Обертання на 20°")
plt.legend()

#збереження у графічний файл
output_file = os.path.join(os.path.expanduser("~"), "Desktop", "output_plot.png")
if not os.access(os.path.dirname(output_file), os.W_OK):
    output_file = "output_plot.png"

plt.savefig(output_file, dpi=100)
print(f"Графік збережено у файл: {output_file}")
