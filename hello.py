from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write('<h1>Hello,Tronado</h1>')


if __name__ == '__main__':
    # 创建web应用
    app = Application(handlers=[
        ('/', IndexHandler)
    ])
    # 绑定端口
    app.listen(8000)
    # 启动Web服务
    print('starting http://localhost:%s' % 8000)
    IOLoop.current().start()
