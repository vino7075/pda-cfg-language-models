import unittest
from pda_cfg import accepts_a_n_b_n, accepts_parentheses, accepts_nested_blocks

class PDATests(unittest.TestCase):
    def test_equal_ab(self):
        self.assertTrue(accepts_a_n_b_n("ab"))
        self.assertTrue(accepts_a_n_b_n("aaaabbbb"))
        for value in ("", "aab", "abb", "ba", "aabbx"):
            self.assertFalse(accepts_a_n_b_n(value))

    def test_parentheses(self):
        self.assertTrue(accepts_parentheses(""))
        self.assertTrue(accepts_parentheses("(()())"))
        for value in (")(", "(()", "())", "(a)"):
            self.assertFalse(accepts_parentheses(value))

    def test_nested_blocks(self):
        self.assertTrue(accepts_nested_blocks("BEGIN x END"))
        self.assertTrue(accepts_nested_blocks("BEGIN x; BEGIN y; END END"))
        for value in ("BEGIN x", "END", "BEGIN BEGIN x END", "BEGIN @ END"):
            self.assertFalse(accepts_nested_blocks(value))

if __name__ == "__main__":
    unittest.main()
