from test_appium_po_1.pages.main_page import MainPage


class TestXueqiu():
    def setup(self):
        self.mp = MainPage()


    def test_add(self):
        self.sp = self.mp.go_to_search()
        self.sp.search("格力电器")
        str = self.sp.add()
        assert "加自选" == str

    def test_add_again(self):
        self.sp = self.mp.go_to_search()
        self.sp.search("格力电器")
        str = self.sp.add()
        assert "设自选" == str
    def test_delete_and_asser(self):
        self.cp = self.mp.go_to_chose_page()
        self.cp.delete("格力电器")