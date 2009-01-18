# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import utils

def prepare(content, theme, resource_fetcher, log):
    theme('#nav').empty()
    theme('#subnav').empty()
    theme('#sidebar').html('<div id="wsgi_menu"></div>')
    theme('#sidebarright').empty()
    theme('#content').empty()

def twocolumns(content, theme, resource_fetcher, log):
    theme('#content').attr.id = 'contentnorightbar'
    theme('#col2').remove()

def nocolumns(content, theme, resource_fetcher, log):
    theme('#content').attr.id = 'contentnobar'
    theme('#col1').remove()
    theme('#col2').remove()

def photos(content, theme, resource_fetcher, log):
    portlets = content('.portlet')
    for p in portlets:
        utils.fixnav(p, theme)

def plone(content, theme, resource_fetcher, log):
    theme('#sidebar').empty()
    content('.documentActions').remove()
    col1 = content('#portal-column-one')
    portlets = col1('.portlet')
    for p in portlets:
        utils.fixnav(p, theme)

def trac(content, theme, resource_fetcher, log):
    theme('#sidebar').empty()
    utils.remove(content, 'br')
    nav = pq('<h2>Trac</h2><ul class="subnav"></ul>')
    menu = nav('ul')
    items = content('#mainnav li')
    for i in items:
        i = pq(i)
        i.attr(class_='__no_css')
        menu.append(i)
    theme('#sidebar').append(nav)

def docs(content, theme, resource_fetcher, log):
    nav = pq('<h2>Association</h2><ul id="docs_nav" class="subnav"></ul>')
    theme('#sidebar').append(nav)

def wiki(content, theme, resource_fetcher, log):
    header = content('#header')
    utils.remove(content, '#username', '#logo', '#searchform', '#footer')
    nav = pq('<h2>Wiki</h2><ul class="subnav"></ul>')
    menu = nav('ul')
    items = header('li')
    for i in items:
        menu.append(pq(i))
    theme('#sidebar').append(nav)
    header.remove()
    for i in content('img'):
        i = pq(i)
        i.attr.src = i.attr.src.replace(':8096', '')

