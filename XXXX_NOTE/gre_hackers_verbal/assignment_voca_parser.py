import datetime
import os

from XXXX_NOTE.AmgheegohraeFormatter import AmgheegohraeFormat

gohrae = AmgheegohraeFormat()
assignment_url = "C:/Users/Hubris Ozymandias/PycharmProjects/datastructure_and_algorithm_in_python/XXXX_NOTE/gre_hackers_verbal/HWs/"
assignment_file_name_list = os.listdir(path=assignment_url)

for assignment_file_name in assignment_file_name_list:

    temp_assignment_url = assignment_url + assignment_file_name

    assignment_word_dict = {
        'chapter_name': assignment_file_name.split('.')[0]
    }
    assignment_voca_list = []
    assignment_raw = open(
        temp_assignment_url,
        'r',
        encoding='UTF8'
    )

    while True:
        line = assignment_raw.readline()
        if line:
            line_split_list = line.split(':')
            if len(line_split_list) > 1:
                if '답' not in line_split_list[0]:
                    word_list = line_split_list[0].split('\t')[-1].split(' ')[1:]
                    for i in range(len(word_list)):
                        if isinstance(word_list[i], str):
                            word_list[i] = word_list[i].lower()
                    word = ' '.join(word_list)
                    meaning = line_split_list[1].split('\n')[0]
                    assignment_voca_list.append([word, meaning])
        else:
            break
    assignment_word_dict['word_list'] = assignment_voca_list
    gohrae.add_word_dict(assignment_word_dict)

# print(gohrae)
excel_file_name = 'GRE Verbal HW '
today = datetime.datetime.today()
excel_file_name += today.strftime('%m%d')

gohrae.save_in_excel(excel_file_name)