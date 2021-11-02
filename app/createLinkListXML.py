import os
import threading
import time
import xml.etree.cElementTree as elemTree_
from pathlib import Path
from app import clickOnLink
from app import browserStatus

event_: threading.Event = threading.Event()
set_thread_ = threading.Thread()
set_thread_.start()

path_to_dir_ = Path('../linksListFile')
path_to_file_ = Path('../linksListFile/LinksList.xml')
web_driver = browserStatus.BrowserStatus.wbd_

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
    #    waitPopUpBox.WaitBox()
    except IOError as ioe:
        print(path_to_file_ + " DOESN'T EXIST IN SYSTEM")
        web_driver.quit()
        print(ioe)


def create_xml(link_list_):
    prepare_file()
    time.sleep(1)
    while not event_.isSet():
        time.sleep(1)
        print("create_xml begins")
        count3 = 0
        try:
            if os.path.exists('../linksListFile/LinksList.xml'):
                print("OK, path exists")
                event_.set()
            else:
                count3 += 1
                prepare_file()
                if count3 < 3 and os.path.exists('../linksListFile/LinksList.xml'):
                    print("OK, path exists, third attempt")
                    event_.set()
                if count3 == 3:
                    print("Creating file failed")
                    web_driver.quit()
                    break
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
    print("Create XML is done")
    print("Here is a list of the links:\n " + str(link_list_))
    time.sleep(0.5)
    clickOnLink.visit_links()


