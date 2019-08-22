from tornado.web import UIModule
from utils.conn import session
from mainapp.models.menu import Menu


class MenuModule(UIModule):
    def render(self, *args, **kwargs):
        data = {
            'menus': session.query(Menu).filter(Menu.parent_id.is_(None)).all(),
            'menus_li': session.query(Menu).filter_by(parent_id=1).all()
        }
        return self.render_string('/', **data)

class Ul_LiModule(UIModule):
    def render(self, *args, **kwargs):
        data = {
            'menus': session.query(Menu).filter(Menu.parent_id.is_(None)).all(),
            'menus_li': session.query(Menu).filter_by(parent_id=1).all(),
            'menus_li2':session.query(Menu).filter_by(parent_id=2).all()
        }
        return self.render_string('menus_ms.html', **data)