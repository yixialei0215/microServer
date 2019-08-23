import random
import time

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class RobbitHandler(RequestHandler):
    def get(self):
        self.render('msg/robbit.html')


class MessageHandler(WebSocketHandler):
    # 当前处理器是一个长连接
    online_clients = []
    def send_all(self,msg):
        for client in self.online_clients:
            # 向客户端发送消息
            client.write_message(msg)

    def open(self):  # 表示客户请求连接
        ip = self.request.remote_ip
        username = self.get_secure_cookie('username').decode()

        self.online_clients.append(self)
        msg = '%s 连接到服务器--%s'%(username,ip)

        self.send_all(msg)



    def on_message(self, message):
        # ip = self.request.remote_ip
        username = self.get_secure_cookie('username').decode()
        msg = '%s 说 : %s' % (username, message)
        self.send_all(msg)


class MessageHandler1(WebSocketHandler):
    # 当前处理器是一个长连接

    def open(self):  # 表示客户请求连接
        ip = self.request.remote_ip

        # 向客户端发送消息
        self.write_message('您好,%s' % ip)

        # 没间隔一秒发送一个幸运数字
        self.write_message('starting')
        for i in range(7):
            time.sleep(1)
            number = random.randint(1, 27)
            self.write_message('您的幸运数字%s' % number)
        self.write_message('end')
