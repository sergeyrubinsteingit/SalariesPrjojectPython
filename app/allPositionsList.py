# -*- coding: utf-8 -*-

position_lst_: list = []
position_flg_: bool = False


def position_list(_position_nm_, _position_flg_):
    # position_lst_.append(_position_nm_)

    # from app import analyzeTableContent
    if position_flg_ is False:
        position_lst_.append(_position_nm_)
        print('((((((( position_flg_ is ' + str(position_flg_) + ' )))))))')
    else:
        print('%%%%% !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! %%%%%%%%%%%%\n')
        print('From allPosition... Position list: \n' + str(position_lst_))

