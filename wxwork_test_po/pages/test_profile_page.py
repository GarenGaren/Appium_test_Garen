from wxwork_test_po.pages import wxwork_page, contact_page


class Test_profile_page():
    def setup(self):
        self.work = wxwork_page()


    def test_add_member(self):
        contact:contact_page = contact_page(self.work)
        contact.add_people("richrich","2","123465@qq.com")

