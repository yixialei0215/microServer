from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        data = {
            'msg': 'Hi,Disen,西安欢迎您',
            'error_msg': '你来错地方了',
            'age': 20,
            'menus': ['主页', '最新推荐', '热门评价'],
            'code': '<h3>h1,我是图片:8>5</h3>'
        }
        self.render('lis.html', **data)

    def post(self, *args, **kwargs):
        # 请求参数的读取
        # 1. 读取单个参数
        wd = self.get_argument('wd')
        print(wd)
        # 2.读取多个参数名相同的参数值
        titles = self.get_arguments('title')
        print(titles)

        # 3. 从查询参数中读取url路径参数
        wd2 = self.get_query_arguments('wd')
        print(wd2)

        titles2 = self.get_query_arguments('title')
        print(titles2)
        self.write('<h3>我是主页中的%s,%s</h3>' % (wd, titles))

        # 4.从请求对象中读取参数
        req: HTTPServerRequest = self.request

        # request请求中的数据都是dick字典类型
        wd3 = req.arguments.get('wd')
        print(wd3)  # 字典key对应的value都是bytes字节类型

        wd4 = req.query_arguments.get('title')
        print(wd4)

    def put(self, *args, **kwargs):
        # 新增数据
        # 读取表单参数u
        # wd1 = self.get_arguments('name')
        # wd2 = self.get_arguments('city')

        # 建议使用
        name = self.get_body_arguments('name')
        city = self.get_body_argument('city')

        self.write('<h3>我是POST请求中的%s,%s</h3>' % (name, city))
