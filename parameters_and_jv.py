from light_intensity_parameters import reorganize_data
from light_intensity_jv import jv

import os


if __name__ == "__main__":
    device_ids = ['1', '6', '12', '13']

    abs_dir_path = os.path.dirname(os.path.realpath(__file__))  # abosolute path of the current .py file
    source_dir = os.path.join(abs_dir_path, "data", "light intensity 20210628")
    target_dir = os.path.join(source_dir, "after_processing")
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    reorganize_data(device_ids, source_dir, target_dir)
    jv(device_ids, source_dir, target_dir)

