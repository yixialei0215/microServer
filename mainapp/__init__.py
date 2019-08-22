from tornado.web import Application
from mainapp.views.cookie_v import CookieHandler
from mainapp.views.index_hander import IndexHandler
from mainapp.views.order_v import OrderHandeler
from mainapp.views.serach_v import SearchHandler


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandeler)
    ], default_host=host)
