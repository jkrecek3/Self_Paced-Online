#!/usr/bin/env python3
"""
pytest module for testing html_render
Author: JohnR
Version: .9
Last updated: 2/04/2019
Notes:
"""

import pytest
import html_render as hr
from io import StringIO as sio


@pytest.mark.smoke  # not sure why this isn't working
def test_element():
    test01 = hr.Element('text foo', style="text-align: center;"
                                          " font-style: oblique;")
    assert test01.content == ['text foo']
    assert test01.indent == ' '
    assert test01.tag == ''
    assert test01.kwargs == {'style': 'text-align: center;'
                                      ' font-style: oblique;'}


def test_append():
    test02 = hr.Element('test02')
    test02.append('test append method')
    assert test02.content == ['test02', 'test append method']


def test_render():
    test03 = hr.Element('test03')
    test03.tag = 'html'
    foo = sio()
    test03.render(foo)
    assert foo.getvalue() == '<html>\ntest03\n</html>\n'


def test_onelinetag():
    test04 = hr.OneLineTag('test04')
    test04.tag = 'title'
    foo = sio()
    test04.render(foo)
    assert foo.getvalue() == '<title>test04</title>\n'


def test_add_items():
    test05 = hr.Element('test05')
    foo = sio()
    test05.add_items(foo)
    assert foo.getvalue() == 'test05\n'


def test_add_items_no_line():
    test06 = hr.Element('test06')
    foo = sio()
    test06.add_items_no_line(foo)
    assert foo.getvalue() == 'test06'


# TODO: create a real test here
def test_add_values():
    pass




