import datetime
import os
import shutil


# function to change directory
def ch_dir(path_dir):
    os.chdir(path_dir)
    print('\nDirectory was changed.')
    
# creating file function
def create_file(name, text = None):
        with open(name, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)

# creating folder function
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('\nFolder exist!\n{}'.format(20 * '*'))

# show current directory
def get_cwd():
    os.getcwd()

# show folder list function
def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)
    
# remove file function
def remove_file(file):
    if os.path.isdir(file):
        try:
            os.rmdir(file)
        except FileNotFoundError:
            print('Folder not exist or was deleted.')
    else:
        os.remove(file)
        
# copy folder or file
def copy_function(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Folder exist!\n{}'.format(20 * '='))
    else:
        shutil.copy(name, new_name)

# function to create file with date and time
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'\n{current_time} - {message}'
    # write to file
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

# module to use funtions
if __name__ == '__main__':
    #create_file('text.txt')
    #create_folder('new_f')
    #get_list()
    #get_list(True)
    #remove_file('new_f')
    #remove_file('file.txt')
    #create_file('text.txt', 'hellpp')
    #create_folder('new_f')
    #copy_function('new_f', 'new_2_f')
    #copy_function('file.txt', 'new_file.txt')
    #ch_dir('c:\\Users\\PC\\Desktop'),
    save_info('message')