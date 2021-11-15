##############################################
# Deletes old jsons. Reads links in
# [linksListFile/LinksList.xml] and opens them.
##############################################
import os
import shutil
import time
import xml.etree.ElementTree as elemenTree
from app.openLinksAsTabs import open_link
from pathlib import Path

all_links_ = []
links_count_: int = 0


def visit_links():
    from app import display_Console
    display_Console.print_console()
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ clickOnLink.py ] :\n'
        '[ visit_links() ] begins.\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    # from app.display_Console import start_printing
    clear_old_jsons()
    global links_count_
    try:
        path_to_file_ = Path('../linksListFile/LinksList.xml')
        get_tree = elemenTree.parse(path_to_file_)
        get_root = get_tree.getroot()
        for links_ in get_root:
            all_links_.extend(links_)
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'From [ clickOnLink.py ] :\n'
                'Total of links: ' + str(all_links_.__len__()) + '.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

            # start_printing()
            for link_ in links_:
                this_link_: str = link_.text
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                    'From [ clickOnLink.py ] :\n'
                    'Link nmb. ' + str(links_count_) + ' is visited.\n\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                open_link(links_count_, this_link_)
                links_count_ += 1
    except FileExistsError:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ clickOnLink.py ] :\n'
            'FileExistsError = ' + str(FileExistsError) + '.\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ clickOnLink.py ] :\n'
        'Total of links: ' + str(all_links_.__len__()) + '.\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')


def clear_old_jsons():
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ clickOnLink.py ] :\n'
        'Deleting jsons from the former test.\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    # clear directory for new files
    try:
        path_to_dir_ = Path('../json_files')
        shutil.rmtree(path_to_dir_)
        time.sleep(0.1)
        os.mkdir(path_to_dir_)
        time.sleep(0.1)
    except FileNotFoundError:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ clickOnLink.py ] :\n'
            'No json files to clear up.\n\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        pass
