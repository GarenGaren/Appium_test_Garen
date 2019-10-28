from wxwork_test_po.pages.contact_page import ContactPage
from wxwork_test_po.pages.wxwork_page import WXworkPage


class TestProfilePage():
    def setup(self):
        self.work = WXworkPage()


    def test_add_member(self):
        contact:ContactPage = ContactPage(self.work)
        contact.add_people("richrich","2","123465@qq.com")

