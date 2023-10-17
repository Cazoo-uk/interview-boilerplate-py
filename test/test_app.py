from src.app import main


class TestApp:
    def test_should_assert_true(self):
        assert main() is True
