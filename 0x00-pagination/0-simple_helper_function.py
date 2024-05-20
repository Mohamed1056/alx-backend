#!/usr/bin/env python3
'''
pagination helper

'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Retrive the index range
    for a given page and page size.
    '''
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
