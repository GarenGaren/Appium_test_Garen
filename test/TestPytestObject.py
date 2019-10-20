import logging


class TestPytestObject:
    def setup_class(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("setup is exc")
    def test_one(self):
        assert 1<2
    def test_two(self):
        assert True