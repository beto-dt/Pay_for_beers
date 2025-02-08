import unittest
from datetime import datetime, timezone
from backend.app.core.entities.stock import Stock, Friend
from backend.app.core.use_cases.list_friend import list_friend


class TestListFriend(unittest.TestCase):

    def setUp(self):
        self.friend1 = Friend(name="John", orders=[])
        self.friend2 = Friend(name="Alice", orders=[])
        self.stock_with_friends = Stock(
            last_update=datetime.now(timezone.utc),
            beers=[],
            friends=[self.friend1, self.friend2]
        )
        self.stock_without_friends = Stock(
            last_update=datetime.now(timezone.utc),
            beers=[],
            friends=[]
        )

    def test_list_friend_with_friends(self):
        result = list_friend(self.stock_with_friends)
        self.assertEqual(len(result), 2)
        self.assertIn(self.friend1, result)
        self.assertIn(self.friend2, result)

    def test_list_friend_without_friends(self):
        result = list_friend(self.stock_without_friends)
        self.assertEqual(len(result), 0)

    def test_list_friend_returns_correct_instance(self):
        result = list_friend(self.stock_with_friends)
        for fr in result:
            self.assertIsInstance(fr, Friend)


if __name__ == "__main__":
    unittest.main()
