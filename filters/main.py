from filters import rotated_image, create_wave_filter, create_image_tile, twist_filter, apply_glass_filter
from slideshow import run_slideshow
from use_filters import apply_random_function
import os

folder_path = 'images'


functions_list = [rotated_image, create_wave_filter, create_image_tile, twist_filter, apply_glass_filter]


if __name__ == '__main__':
    files = os.listdir(folder_path)
    objects = ['images/' + i for i in files]
    images_done = apply_random_function(objects, functions_list)
    run_slideshow(images_done, 4)
