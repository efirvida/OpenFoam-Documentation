#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import re
from glob import glob

H_FILES_DIR = "c:\\Program Files\\blueCFD-Core-2016\\OpenFOAM-4.x\\src\\"
DOC_FILES_DIR = '.' + os.sep


FILE_LIST = (y for x in os.walk(H_FILES_DIR)
             for y in glob(os.path.join(x[0], '*.H')))


def GetFileHeaader(h_file):
    with open(h_file) as f:
        text_lines = f.readlines()

    def match(s): return True if '\*' and '*/\n' in s else False

    doc_begin = filter(lambda x: 'Class\n' in x[1], enumerate(text_lines))
    doc_end = filter(lambda x: match(x[1]), enumerate(text_lines))

    if doc_begin and doc_end:
        return text_lines[doc_begin[0][0]:doc_end[0][0]]
    else:
        return


def _mkdir_recursive(path):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        _mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)


def _format_MARKDOWN(text):
    for line, line_text in enumerate(text):
        if line_text == '\n':
            continue
        if line_text[0] != ' ':
            text[line] = '## %s' % line_text
            continue
        if '    ' in line_text and '     ' not in line_text:
            text[line] = line_text.replace('    ', '')
        if 'erbatim\n' in line_text:
            text[line] = '```\n'
            continue
        if '\\table' in line_text:
            text[line] = '\n'
            continue
        if '\endtable' in line_text:
            text[line] = '\n'
            continue
        # if line_text.count('|'):
        #     text[line] = '|' + % line_text

        # if '<a href=' in line_text:
        #     text[line] = line_text.replace('<a href=', '[')
        #     continue
        # if '<\a>' in line_text:
        #     text[line] = line_text.replace('</a>', ']')
        #     continue

    return text


for h_file in FILE_LIST:
    def _file(the_file): return os.path.split(os.path.abspath(the_file))

    doc_text = GetFileHeaader(h_file)
    DOC_FILE = _file(h_file.replace(H_FILES_DIR, DOC_FILES_DIR))

    if doc_text:
        _mkdir_recursive(DOC_FILE[0])
        with open(os.sep.join(DOC_FILE).replace('.H', '.md'), 'w') as f:
            _format_MARKDOWN(doc_text)
            doc_text.insert(0, '# %s \n' % DOC_FILE[1].replace('.H', ''))
            f.writelines(doc_text)


MD_FILE_LIST = (y for x in os.walk(DOC_FILES_DIR)
                for y in glob(os.path.join(x[0], '*.md')))

with open(DOC_FILES_DIR + 'README.md', 'w') as f:
    text = []
    for m_file in MD_FILE_LIST:
        levels = m_file.replace(DOC_FILES_DIR, '').count(os.sep)
        if levels < 3:
            text.append( ' * ' + '#' * levels + ' [%s](./%s)\n' % (
                                    m_file.split(os.sep)[-1].replace('.md', ''),
                                    m_file.replace(DOC_FILES_DIR, '').replace(os.sep,'/')))
        else:
            text.append('%s[%s](./%s)\n' % (m_file.count(os.sep)*' ' + '- ',
                        m_file.split(os.sep)[-1].replace('.md', ''),
                        m_file.replace(DOC_FILES_DIR, '').replace(os.sep, '/')))
    text[0] = "# Index\n"
    f.writelines(text)

print ':: Done ::'
