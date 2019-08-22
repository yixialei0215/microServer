from mainapp import make_app
import tornado.options as options
import tornado.ioloop

if __name__ == '__main__':
    # 定义命令行参数
    options.define('port',
                   default=8000,
                   type=int,
                   help='bind socket port')
    options.define('host',
                   default='localhost',
                   type=str,
                   help='设置host name')
    # 解析命令行参数
    options.parse_command_line()

    app = make_app(options.options.host)

    app.listen(options.options.port)  # 使用命令行参数

    print('starting Web Server http://%s:%s' % (tornado.options.options.host, tornado.options.options.port))
    # 启动服务
    tornado.ioloop.IOLoop.current().start()
