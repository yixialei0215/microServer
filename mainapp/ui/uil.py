from tornado.web import UIModule


class UlModule(UIModule):
    def render(self, *args, **kwargs):
        data = {
            'ul': ['导航', '插件']
        }
        return self.render_string('ui/ui.html', **data)
