from unittest import TestCase

from utils.conn import session
from mainapp.models.menu import Menu


class TestMenuORM(TestCase):
    def test_add(self):
        m1 = Menu()
        m1.title = '用户管理'

        session.add(m1)
        session.commit()

    def test_adds(self):
        session.add_all([
            Menu(title='订单管理'),
            Menu(title='会员管理', url='/user1', parent_id=1),
            Menu(title='派件员', url='/user2', parent_id=1),
            Menu(title='合作商', url='/user3', parent_id=1),
            Menu(title='订单统计', url='/order_cnt', parent_id=2),
        ])
        session.commit()

    def test_get(self):
        # 查询-session.query(模型类)
        m = session.query(Menu).get(1)
        print(m.title)
        print('------查看所有的子菜单------')
        for cm in m.childs:
            print(cm)

    def test_query_root_menu(self):
        # 查看所有的一级菜单
        m = session.query(Menu).filter_by(parent_id=None).all()
        for ml in m:
            print(ml.title)
            for ms in ml.childs:
                print("---",ms)


    def test_delete(self):
        m1 = session.query(Menu).get(1)
        session.delete(m1)
        session.commit()

    def test_update(self):
        m1 = session.query(Menu).get(1)
        m1.title = '商品管理'
        session.commit()
