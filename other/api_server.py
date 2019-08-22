import json
import uuid

from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line


class LoginHandler(RequestHandler):
    users = [{
        'id': 1,
        'name': 'disen',
        'pwd': '123',
        'last_login_device': 'Android 5.1 Oneplus5'
    }]

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST,DELETE,PUT')

    def get(self):
        # 读取json数据
        bytes = self.request.body

        # 从请求头中读取请求上传的类型
        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)

            resp_data = {}
            login_user = None
            for user in self.users:
                if json_data['name'] == user['name']:
                    if json_data['pwd'] == user['pwd']:
                        login_user = user
                        break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此用户'

            self.set_header('Content-Type', 'application/json')
            self.write(resp_data)
        else:
            self.write('uploda data 必须是json类型')

    def post(self, *args, **kwargs):
        bytes = self.request.body

        # 从请求头中获取请求上传的类型
        content_type = self.request.headers.get('Content-Type')

        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)

            name = json_data['name']
            pwd = json_data[('pwd')]
            phone = json_data[('phone')]
            last_login_device = json_data.setdefault('last_login_device', 'PC')

            resp_data = {}
            if all((name, pwd)):
                yonghu = {
                    'id': self.users[len(self.users) - 1]['id'] + 1,
                    'name': name,
                    'pwd': pwd,
                    'phone': phone,
                    'last_login_device': last_login_device
                }
                self.users.append(yonghu)
                resp_data['msg'] = '添加成功'
                resp_data['user'] = self.users
                print(self.users)
            else:
                resp_data['msg'] = '添加失败'
                self.write('填写正确的用户名或者密码')

            self.set_header('Content', 'application/json')
            self.write(resp_data)
        else:
            print('请上传正确的类型')

    def put(self):
        bytes = self.request.body

        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)
            resp_data = {}
            for u in self.users:
                if u['id'] == int(json_data['id']):
                    for kay, value in json_data.items():
                        u[kay] = value
                    resp_data['msg'] = '修改成功'
                    resp_data['user'] = self.users
                else:
                    resp_data['msg'] = '您输入的信息不存在，请重新输入'
            self.set_header('Content-Type', 'application/json')
            self.write(resp_data)
        else:
            self.write('请输入正确的类型')

    def delete(self, *args, **kwargs):
        bytes = self.request.body

        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)

            resp_data = {}
            for u in self.users:
                if u['id'] == int(json_data['id']):
                    index = int(json_data['id']) - 1
                    self.users.remove(u)

                    resp_data['msg'] = '删除成功'
                    resp_data['user'] = self.users
                else:
                    resp_data['msg'] = '请输入正确的信息'

                self.set_header('Content-Type', 'application/json')
                self.write(resp_data)

        else:
            print('请输入正确的格式')

    def options(self, *args, **kwargs):
        self.set_status(200)

    def on_finish(self):
        pass


def make_app():
    return Application(
        handlers=[
            ('/user', LoginHandler)
        ],
        default_host=options.h)


if __name__ == '__main__':
    #  绑定命令行参数
    define('p', default=8000, type=int, help='绑定的port端口')
    define('h', default='localhost', type=str, help='绑定的主机IP')

    # 解析命令行参数
    parse_command_line()

    app = make_app()
    app.listen(options.p)

    print('Running http://%s:%s' % (options.h, options.p))
    IOLoop.current().start()
