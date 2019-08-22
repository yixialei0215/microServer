import tornado.web as web
import tornado.ioloop as ioloop
from tornado.options import define, options, parse_command_line

# 定义命令行的参数
define('port', default=8000, type=int, help='我就是金咕咕')


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('粉丝们，么么哒！！')


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('2017年春季赛MVP，2018年春季赛MV第二名，2019年夏季赛MVP，去年的克烈，今年的潘森')


class LogoutHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        word = self.get_argument('wd')
        self.write('6666 <p>查询参数wd:%s</p>' % word)

    def post(self, *args, **kwargs):
        word = self.get_argument('wd')
        self.write('Post methon:Hi,tornado <p>表单参数wd:%s</p>' % word)


if __name__ == '__main__':
    # 解析命令行中参数
    parse_command_line()

    # 声明Web服务中请求资源
    app = web.Application([
        ('/', IndexHandler),
        ('/login', LoginHandler),
        ('/logout', LogoutHandler)
    ])

    # 使用命令行中的参数 port
    app.listen(options.port)

    ioloop.IOLoop.current().start()
