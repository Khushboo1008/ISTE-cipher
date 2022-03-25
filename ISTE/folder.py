import os
import random
path = 'C:\\Users\\khush\\Documents\\GitHub\\ISTE-cipher\\Dummy'
chars = 'qwertyuiopasdfghjklzxcvbnm'

def get_rand_str (n):
    return ''.join(random.choice(chars) for _ in range(n))
    
def create_folder(n):
    for _ in range(0,n):
        os.mkdir(f'{path}//{get_rand_str(10)}')

    all_folders = os.listdir(path)
    for folder in all_folders:
        file = open(f'{path}\\{folder}\\{get_rand_str(10)}.txt','w')
        file.write('Wrong File, Please try again')

create_folder(499)