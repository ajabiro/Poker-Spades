import unittest
import spadesfunctions


# TESTING THE 3 CARDS AND THE SECOND SPOT IS WHAT THE EXPECTED RETURN VALUE IS
class MyTestCase(unittest.TestCase):
    def test_if_a_straight1(self):
        self.assertEqual(spadesfunctions.check_straight('S8', 'S10', 'S9'), 10)

    def test_if_a_straight2(self):
        self.assertEqual(spadesfunctions.check_straight('SJ', 'SQ', 'SK'), 13)

    def test_if_a_straight3(self):
        self.assertEqual(spadesfunctions.check_straight('S6', 'S8', 'S10'), 0)

    def test_if_a_straight4(self):
        self.assertEqual(spadesfunctions.check_straight('SQ', 'SK', 'SA'), 14)

    def test_if_a_straight5(self):
        self.assertEqual(spadesfunctions.check_straight('SA', 'SA', 'S3'), 0)

    def test_if_3_of_a_kind1(self):
        self.assertEqual(spadesfunctions.check_3ofa_kind('S9', 'S9', 'S9'), 9)

    def test_if_3_of_a_kind2(self):
        self.assertEqual(spadesfunctions.check_3ofa_kind('S7', 'S9', 'SJ'), 0)

    def test_if_3_of_a_kind3(self):
        self.assertEqual(spadesfunctions.check_3ofa_kind('SQ', 'SQ', 'SQ'), 12)

    def test_if_3_of_a_kind4(self):
        self.assertEqual(spadesfunctions.check_3ofa_kind('SA', 'S3', 'S4'), 0)

    def test_if_3_of_a_kind5(self):
        self.assertEqual(spadesfunctions.check_3ofa_kind('S4', 'S4', 'S4'), 4)

    def test_if_royal_flush1(self):
        self.assertEqual(spadesfunctions.check_royal_flush('S5', 'S6', 'S7'), 0)

    def test_if_royal_flush2(self):
        self.assertEqual(spadesfunctions.check_royal_flush('SQ', 'SK', 'SA'), 14)

    def test_if_royal_flush3(self):
        self.assertEqual(spadesfunctions.check_royal_flush('SA', 'S8', 'S6'), 0)

    def test_if_royal_flush4(self):
        self.assertEqual(spadesfunctions.check_royal_flush('SK', 'SQ', 'SA'), 14)

    def test_play_cards1(self):
        self.assertEqual(spadesfunctions.play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), 1)

    def test_play_cards2(self):
        self.assertEqual(spadesfunctions.play_cards('S4', 'S4', 'S4', 'S2', 'S4', 'S3'), 1)

    def test_play_cards3(self):
        self.assertEqual(spadesfunctions.play_cards('S4', 'S4', 'S4', 'S3', 'S3', 'S3'), -1)

    def test_play_cards4(self):
        self.assertEqual(spadesfunctions.play_cards('S5', 'S6', 'S7', 'S10', 'S10', 'S10'), -1)

    def test_play_cards5(self):
        self.assertEqual(spadesfunctions.play_cards('S2', 'S4', 'S3', 'S10', 'SJ', 'SQ'), 1)

    def test_play_cards6(self):
        self.assertEqual(spadesfunctions.play_cards('SA', 'SA', 'SA', 'SJ', 'SJ', 'SJ'), -1)

    def test_play_cards7(self):
        self.assertEqual(spadesfunctions.play_cards('S8', 'S9', 'S7', 'S7', 'S9', 'S8'), 0)

    def test_play_cards8(self):
        self.assertEqual(spadesfunctions.play_cards('SA', 'SA', 'SA', 'SQ', 'SK', 'SA'), 1)

    def test_play_cards9(self):
        self.assertEqual(spadesfunctions.play_cards('S2', 'S3', 'S4', 'S8', 'S8', 'S8'), -1)

    def test_play_cards10(self):
        self.assertEqual(spadesfunctions.play_cards('S4', 'S4', 'S4', 'S4', 'S4', 'S4'), 0)



if __name__ == '__main__':
    unittest.main()
