# -*- coding: utf-8 -*-
import os
from pyquery import PyQuery as pq

def get_theme(req, resp, log):
    if '/forum' in req.path_info:
        return "/theme/twocolumns.html"
    return "/theme/index.html"

PROX = dict(
        membres=10,
        planet=10,

        trac=20,

        wiki=30,

        docs=40,
        photos=40,
        association=40,
     )

PROX_TEMPLATE = os.environ.get('DEBUG', None) and 'http://wsgi.afpy.org:110%s/%s' or 'http://localhost:100%s/%s'

def get_proxy(req, log):
    name = req.script_name[1:]
    if name == 'planet':
        return 'http://ziade.org/afpy'
    port = PROX.get(name, None)
    prox = PROX_TEMPLATE % (port, name)
    return prox

def match_notheme(req, resp, headers, *args):
    match = False
    if req.headers.get('X-Requested-With', '').startswith('XML'):
        resp.body = resp.body.replace('<html><body>', '').replace('</body></html>', '')
        match = True
    if 'notheme' in req.params:
        match = True
    return match

def fixnav(p, theme):
    p = pq(p)
    title = p('h5').text()
    items = p('div.nav1')('a')
    if items:
        nav = pq('<h2>%s</h2><ul class="subnav"></ul>' % title)
        menu = nav('ul')
        for i in items:
            menu.append('<li>%s</li>' % str(pq(i)))
        theme('#sidebar').append(nav)

def remove(doc, *args):
    for selector in args:
        doc(selector).remove()

