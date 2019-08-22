import os

from tornado.web import Application

from mainapp.views.cookie_v import CookieHandler
from mainapp.views.index_hander import IndexHandler
from mainapp.views.order_v import OrderHandeler
from mainapp.views.serach_v import SearchHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # E:\microServer

#
settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/'  # 访问资源路径
}


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandeler)
    ], default_host=host, **settings)
