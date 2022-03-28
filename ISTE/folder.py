import os
import random
from fpdf import FPDF
import time

path = 'C:\\Users\\Jai\\Documents\\GitHub\\ISTE-cipher\\ISTE\\Dummy'
chars = 'qwertyuiopasdfghjklzxcvbnm'


def get_rand_str(n):
    return ''.join(random.choice(chars) for _ in range(n))


def create_folder(n):
    for _ in range(0, n):
        os.mkdir(f'{path}//{get_rand_str(10)}')

    all_folders = os.listdir(path)
    for idx, folder in enumerate(all_folders):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Wrong File",
                 ln=1, align='C')
        pdf.cell(200, 10, txt="Please try again",
                 ln=2, align='C')
        pdf.output(f"{path}\\{folder}\\{get_rand_str(10)}.pdf")
        print(folder, idx)
        # file = open(f'{path}\\{folder}\\{get_rand_str(10)}.pdf', 'w')
        # file.write('Wrong File, Please try again')


create_folder(10)
