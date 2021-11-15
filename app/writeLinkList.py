import time


def write_link_list():
    from app import createLinkListXML
    from defaultModule import default_wbd_ as _default_wbd_
    time.sleep(2)
    print('\nBrowser and Links \n####################')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
          'write_link_list():\n'
          'Lists links on the front page to visit and test.\n\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    web_driver_ = _default_wbd_

    # On a front page of the site finds a list of pages
    # available in this site:
    ol_tag_ = web_driver_.find_element_by_xpath('//*[@id="__next"]/div/main/div[3]/div[2]/ol[2]')
    li_tag_ = ol_tag_.find_elements_by_tag_name("li")
    li_tag_list_ = []
    count_: int = 0
    for childNode in range(len(li_tag_)):
        current_li_tag_ = li_tag_[count_]
        link_txt_ = current_li_tag_.find_element_by_tag_name("a")
        li_tag_list_.append(link_txt_.text)
        count_ += 1
    time.sleep(0.5)
    createLinkListXML.create_xml(li_tag_list_)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
          'Calls [ create_xml ] function.\n\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
