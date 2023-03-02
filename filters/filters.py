import math
import random

from PIL import Image


def create_image_tile(image_path, m=2, n=2):
    # Открываем изображение
    with Image.open(image_path) as im:
        # Получаем размеры изображения
        width, height = im.size

        # Вычисляем размеры одного блока с учетом белой границы между блоками
        border_width = 2
        block_width = (width + border_width) // n - border_width
        block_height = (height + border_width) // m - border_width

        # Создаем новое изображение для плитки
        tile_width = n * (block_width + border_width) - border_width
        tile_height = m * (block_height + border_width) - border_width
        tile = Image.new('RGB', (tile_width, tile_height), (255, 255, 255))

        # Добавляем блоки изображения в плитку с белой границей между блоками
        for i in range(m):
            for j in range(n):
                x = j * (block_width + border_width)
                y = i * (block_height + border_width)
                box = (x, y, x + block_width, y + block_height)
                region = im.crop(box)
                tile.paste(region, (x, y))
                if j < n - 1:  # Добавляем белую границу между блоками в строке
                    tile.paste((255, 255, 255), (x + block_width, y, x + block_width + border_width, y + block_height))
                if i < m - 1:  # Добавляем белую границу между блоками в столбце
                    tile.paste((255, 255, 255), (x, y + block_height, x + block_width, y + block_height + border_width))

        # Сохраняем плитку
        tile.save('images_done/image_tile.png')
        return 'images_done/image_tile.png'


def rotated_image(image_path, angle=45):
    with Image.open(image_path) as im:
        rotated_img = im.rotate(angle, expand=True)
        rotated_img.save('images_done/rotated_img.png')
    return 'images_done/rotated_img.png'


def twist_filter(image_path):
    # Открыть изображение
    with Image.open(image_path) as im:
        # Получить размеры изображения
        width, height = im.size

        # Создать новое изображение
        new_im = Image.new("RGB", (width, height), (255, 255, 255))

        # Пройти по каждому пикселю нового изображения
        for y in range(height):
            for x in range(width):
                # Вычислить расстояние до центра изображения
                dx = x - width / 2
                dy = y - height / 2
                dist = math.sqrt(dx * dx + dy * dy)

                # Вычислить угол поворота
                angle = (math.pi / 256) * dist

                # Скрутить пиксель в соответствии с углом поворота
                src_x = int((x - width / 2) * math.cos(angle) - (y - height / 2) * math.sin(angle) + width / 2)
                src_y = int((x - width / 2) * math.sin(angle) + (y - height / 2) * math.cos(angle) + height / 2)

                # Получить цвет пикселя из исходного изображения
                if src_x >= 0 and src_x < width and src_y >= 0 and src_y < height:
                    color = im.getpixel((src_x, src_y))
                else:
                    color = (255, 255, 255)

                # Задать цвет пикселя нового изображения
                new_im.putpixel((x, y), color)

        # Сохранить новое изображение
        new_im.save('images_done/twisted.png')
        return 'images_done/twisted.png'


def create_wave_filter(image_path, amplitude=50, frequency=0.0005):
    # Открываем исходное изображение
    with Image.open(image_path) as im:
        # Получаем размеры исходного изображения
        width, height = im.size

        # Создаем новое изображение для фильтра
        filtered_im = Image.new('RGB', (width, height), (255, 255, 255))

        # Применяем фильтр
        for t in range(height):
            for s in range(width):
                # Получаем цвет пикселя из исходного изображения
                r, g, b = im.getpixel((s, t))

                # Вычисляем новое значение t с учетом волны
                t_new = int(t + amplitude * math.sin(2 * math.pi * frequency * s))

                # Проверяем, не выходит ли новое значение t за границы изображения
                if t_new >= height or t_new < 0:
                    continue

                # Применяем цвет пикселя к новому изображению с учетом измененной координаты t
                filtered_im.putpixel((s, t_new), (r, g, b))

        # Сохраняем новое изображение
        filtered_im.save('images_done/filtered_image.png')
        return 'images_done/filtered_image.png'


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
                rand_x = random.randint(max(0, i - 5), min(width - 1, i + 5))
                rand_y = random.randint(max(0, j - 5), min(height - 1, j + 5))

                # Получаем цвет случайного пикселя
                r, g, b = im.getpixel((rand_x, rand_y))

                # Присваиваем цвет текущему пикселю
                filtered_im.putpixel((i, j), (r, g, b))

        # Сохраняем отфильтрованное изображение
        filtered_im.save('images_done/glass_filter.png')
    return 'images_done/glass_filter.png'
