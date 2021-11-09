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
    clear_old_jsons()
    global links_count_
    try:
        path_to_file_ = Path('../linksListFile/LinksList.xml')
        get_tree = elemenTree.parse(path_to_file_)
        get_root = get_tree.getroot()
        for links_ in get_root:
            all_links_.extend(links_)
            print('clickOnLink: all_links_ length is ' + str(all_links_.__len__()) + '\n')
            for link_ in links_:
                this_link_: str = link_.text
                print('clickOnLinks: links_count_ = ' + str(links_count_) + '\n****************************')
                open_link(links_count_, this_link_)
                links_count_ += 1
    except FileExistsError:
        print('FileExistsError = ' + str(FileExistsError))
    print('clickOnLinks, visit_links(): links nmb is ' + str(all_links_.__len__()) + '\n')


def clear_old_jsons():
    print('--------------- clear_old_jsons() -------------------')
    # clear directory for new files
    try:
        path_to_dir_ = Path('../json_files')
        shutil.rmtree(path_to_dir_)
        time.sleep(0.1)
        os.mkdir(path_to_dir_)
        time.sleep(0.1)
    except FileNotFoundError:
        print('--------------- No json files to clear up -------------------')
        pass
