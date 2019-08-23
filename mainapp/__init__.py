import os

from tornado.web import Application

from mainapp.ui.menu import MenuModule, Ul_LiModule
from mainapp.ui.uil import UlModule
from mainapp.views.cookie_v import CookieHandler
from mainapp.views.donload import DownloadHandler, AsyncDownloadHandler, Async2DownloadHandler
from mainapp.views.index_hander import IndexHandler
from mainapp.views.order_v import OrderHandeler
from mainapp.views.serach_v import SearchHandler
from mainapp.views.message import MessageHandler, RobbitHandler
from mainapp.views.user import UserHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # E:\microServer

#


settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',  # 访问资源路径
    'ui_modules': {
        'Menu': MenuModule,
        'Ui': UlModule,
        'Ul_li': Ul_LiModule
    },
    'cookie_secret': '135asd1g53as13g',
    'xsrf_cookies': True
}


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandeler),
        ('/download2', Async2DownloadHandler),
        ('/download1', AsyncDownloadHandler),
        ('/download', DownloadHandler),
        ('/robbit', RobbitHandler),
        ('/message', MessageHandler),
        ('/login', UserHandler)
    ], default_host=host, **settings)
