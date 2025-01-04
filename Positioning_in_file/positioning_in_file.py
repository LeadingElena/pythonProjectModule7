import io

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    number_of_string = 0
    strings_positions = {}
    for string in strings:
        start_of_line_byte = file.tell()
        number_of_string += 1
        file.write(string + '\n')
        strings_positions[number_of_string, start_of_line_byte] = [string]
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)