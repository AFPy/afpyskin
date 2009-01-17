# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

twocolumns = set(['/trac', '/wiki', '/photo', '/membres'])

def get_theme(req, resp, log):
    if '/forum' in req.path_info:
        return "/theme/twocolumns.html"
    return "/theme/index.html"

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

