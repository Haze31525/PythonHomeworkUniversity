from PIL import Image
import math
from PIL import Image
import math

import random
from PIL import Image

def apply_glass_filter(image_path):
    # Открываем изображение
    with Image.open(image_path) as im:
        # Получаем размеры изображения
        width, height = im.size

        # Создаем новое изображение для отфильтрованного изображения
        filtered_im = Image.new('RGB', (width, height), (255, 255, 255))

        # Применяем фильтр стекло
        for i in range(width):
            for j in range(height):
                # Получаем случайные координаты
                rand_x = random.randint(max(0, i-5), min(width-1, i+5))
                rand_y = random.randint(max(0, j-5), min(height-1, j+5))

                # Получаем цвет случайного пикселя
                r, g, b = im.getpixel((rand_x, rand_y))

                # Присваиваем цвет текущему пикселю
                filtered_im.putpixel((i, j), (r, g, b))

        # Сохраняем отфильтрованное изображение
        filtered_im.save('glass_filter.png')



apply_glass_filter('1626976834_16-kartinkin-com-p-fioletovaya-sakura-anime-anime-krasivo-16.jpg')