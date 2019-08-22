from tornado.web import RequestHandler


class CookieHandler(RequestHandler):
    def get(self):
        # 验证参数中是否存在name?
        if self.request.arguments.get('name'):
            # 从查询参数中读取Cookie的名称
            name = self.get_query_argument('name')

            # 从cookies中获取name的对象
            value = self.get_cookie(name)
            print(type(value))
            self.write(value)
        else:
            # 查看所有的cookies
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:
                lis.append('<li>%s:%s</li>' % (key, self.get_cookie(key)))
            self.write('显示所有cookie' + html % ''.join(lis))
        html1 = """
                <form method='post'>
                    <input type='text' name='name'>
                    <button>提交</button>
                </form>
              """
        self.write(html1)

    def post(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            # 存在，删除
            self.clear_cookie(name)
            self.write('<h3 style"color:green">删除%s成功</h3>' % name)
        else:
            self.write('<h3 style"color:red">删除%s失败,不存在!</h3>' % name)

        # 重定向操作时，不需要在调用self.write()5
        self.redirect('/cookie')
