import os
import platform

# Задание1

# os.uname availoible anly at Unix systems
current_os = platform.platform()
current_path = os.getcwd()

def define_type(container):

    type_dict = {}
    for each in container:
        file_type = each.split(sep='.')
        file_type = [i.lower() for i in file_type]
        print(file_type)
        if file_type[1] == 'heic' or file_type[1] == 'jpg':
            if 'photo' in type_dict:
                type_dict['photo'].append(each)
            else:
                type_dict['photo'] = [each]

        if file_type[1] == 'mov' or file_type[1] == 'mp4':
            if 'movie' in type_dict:
                type_dict['movie'].append(each)
            else:
                type_dict['movie'] = [each]

        if file_type[1] == 'txt' or file_type[1] == 'docx':
            if 'text' in type_dict:
                type_dict['text'].append(each)
            else:
                type_dict['text'] = [each]

    return type_dict

def sort_to_dir(types_dict):

    for key, value in types_dict.items():
        target_directory = os.path.join('test', key)

        if os.path.exists(target_directory):
            [os.replace(os.path.join('test', i), target_directory) for i in value]
        else:
            os.mkdir(target_directory)
            [os.replace(os.path.join('test', i), target_directory) for i in value]
    pass


my_directory = os.path.join('test')
container = [*list(os.listdir(my_directory))]

print(container)
print(define_type(container))

types_dict = define_type(container)
sort_to_dir(types_dict)
