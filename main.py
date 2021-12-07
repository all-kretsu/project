# program file manager
from os import getcwd
from os import name
import sys


from guess_numb import input_num
from guess_numb import play_again_func
from core import ch_dir
from core import copy_function
from core import create_file
from core import create_folder
from core import get_list
from core import remove_file
from core import save_info


# starting program
save_info('\n{}\nStart\n'.format(20 * '='))

command = sys.argv[1]

# program body
# change directory
if command == 'cd':
    cur_dir = getcwd()
    print('\nCurrent directory:\n\t', cur_dir, '\n')
    name = sys.argv[2]
    ch_dir(name)


# show time information
elif command == 'save_inf':
    try:
        name = sys.argv[2]
        save_info(name)
    except IndexError:
        print('Insert command name again!')

# copy file or folder
elif command == 'copy':
    try:
        root_file = sys.argv[2]
        name = sys.argv[3]
        copy_function(root_file, name)
    except IndexError:
        print('Enter file name to copy again!')

# create file
elif command == 'cfile':
    try:
        name_1 = sys.argv[2]
        create_file(name_1)
    except IndexError:
        print('\nInsert file name!')

# create folder
elif command == 'cfolder':
    try:
        name = sys.argv[2]
        create_folder(name)
    except IndexError:
        print('\n--Insert folder name!--')

# the game
elif command == 'game':
    try:
        input_num()
        play_again_func()
    except IndexError:
        print('Insert command name again!')
        
# show list
elif command == 'list':
    get_list()

# remove file
elif command == 'remove':
    try:
        name = sys.argv[2]
        remove_file(name)
    except IndexError:
        print('\n--Insert correct file name!--')
    except FileNotFoundError:
        print('\n--File is not exist!--')

# write file
elif command == 'write':
    try:
        file_name_1 = sys.argv[2]
        file_name_2 = sys.argv[3]
        create_file(file_name_1, file_name_2)
    except IndexError:
        print('\nInsert file name or text!')

# show command list
elif command == 'help':
    print(
        '\nIts a file manager, enter a command to get the function;'.upper()
        )
    print('\nManager commands:\n{}\n'.format(45 * '='))
    print('\t1. "cd": Change directory;\n')
    print('\t2. "copy": Insert name and new name to copy a folder or file;\n')
    print('\t3. "game": To play in "guess number".\n')
    print('\t4. "save_inf": Save information with date and message;\n')
    print('\t5. "cfile": Create file with text;\n')
    print('\t6. "cfolder": Create folder;\n')
    print('\t7. "list": Get the list;\n')
    print('\t8. "write": Write file;\n')
    print('\t9. "remove": Remove file or folder;\n\n{}'.format(45 * '='))

# ending program
save_info('\n{}\nEnd\n'.format(20 * '='))





