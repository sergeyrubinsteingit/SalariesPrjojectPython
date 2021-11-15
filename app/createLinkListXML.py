##############################################
# Stores page link names into XML file list
# for further usage i [clickOnLink.visit_links()]
# to open links.
##############################################
import os
import sys
import threading
import time
import xml.etree.cElementTree as elemTree_
from pathlib import Path
from app import clickOnLink
from defaultModule import default_wbd_ as _default_wbd_

event_: threading.Event = threading.Event()
set_thread_ = threading.Thread()
set_thread_.start()

path_to_dir_ = Path('../linksListFile')
path_to_file_ = Path('../linksListFile/LinksList.xml')
web_driver = _default_wbd_

flg_click_: bool = False


def prepare_file():
    try:
        if os.path.exists(path_to_file_):
            # Deleting the former file and its directory
            os.remove(path_to_file_)
            event_.wait(3)
            os.rmdir(path_to_dir_)
            event_.wait(3)
        # creates a dir
        time.sleep(1)
        path_to_dir_.mkdir(parents=True, exist_ok=True)
        event_.wait(1)
        # Creates a file unless it already exists
        path_to_file_.touch(exist_ok=True)
        event_.wait(1)
    except IOError as ioe:
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ createLinkListXML ] :\n'
            'FILE [ ' + str(path_to_file_) + ' ] DOESN\'T EXIST IN SYSTEM.\n\n' 
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        web_driver.quit()
        print(ioe)


def create_xml(link_list_):
    prepare_file() # creates a new XML file
    time.sleep(1)
    while not event_.isSet(): # Awaits till the [prepare_file()] function creates a new XML file
        time.sleep(1)
        print(
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
            'From [ createLinkListXML ] :\n'
            'Now [ create_xml ] is running.\n\n' 
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        count3 = 0
        try:
            if os.path.exists('../linksListFile/LinksList.xml'):
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                    'From [ createLinkListXML ] :\n'
                    'OK, path to XML exists.\n\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                event_.set()
                break
            else:
                count3 += 1
                prepare_file()
                if count3 < 3 and os.path.exists('../linksListFile/LinksList.xml'):
                    print(
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                        'From [ createLinkListXML ] :\n'
                        'OK, path to XML was found on third attempt.\n\n'
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                    event_.set()
                    break
                if count3 == 3:
                    print("Creating file failed")
                    print(
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                        'From [ createLinkListXML ] :\n'
                        'Sorry, creating of the XML file failed.\n'
                        'Test cannot be continued and shut down.\n\n'
                        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                    web_driver.quit()
                    sys.exit(-1)

        except KeyboardInterrupt:
            event_.set()
            break

    settings_tag_ = elemTree_.Element("settings")
    links_tag_ = elemTree_.SubElement(settings_tag_, "links")
    count2: int = 0
    for list_item in range(len(link_list_)):
        list_item = str(count2)
        elemTree_.SubElement(links_tag_, "link_", name="link_" + list_item).text = link_list_[count2]
        count2 += 1
    tag_tree_ = elemTree_.ElementTree(settings_tag_)
    tag_tree_.write(path_to_file_, encoding="UTF-8", xml_declaration=True)
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
        'From [ createLinkListXML ] :\n'
        'Create XML is done.\n'
        'Here is a list of the links: \n'  + str(link_list_) + '\n\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    time.sleep(0.5)
    clickOnLink.visit_links()
    import app.display_Console
    app.display_Console.print_console() # Sends console info to the Text box to keep tester in touch with the process.



