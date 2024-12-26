import unittest
import main

rows = 6
cols = 6

SUN = 1
MOON = 3
BLANK = 2


class MainTests(unittest.TestCase):
    def test_breachRule2_0(self):
        # no piece
        solution = [[BLANK] * rows for i in range(rows)]
        flag = main.breachRule2(solution)
        self.assertEqual(False, flag)

    def test_breachRule2_1(self):
        # only 1 piece by row or col
        solution = [[BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
                    ]
        flag = main.breachRule2(solution)
        self.assertEqual(False, flag)

    def test_breachRule2_2a(self):
        # only 2 connected by row
        solution = [[BLANK, SUN, SUN, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
                    ]
        flag = main.breachRule2(solution)
        self.assertEqual(False, flag)


    def test_breachRule2_2b(self):
        # only 2 connected by col
        solution = [[BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
                    ]
        flag = main.breachRule2(solution)
        self.assertEqual(False, flag)

    def test_breachRule2_3a(self):
        # 3 connected by row
        solution = [[BLANK, SUN, SUN, SUN, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
                    ]
        flag = main.breachRule2(solution)
        self.assertEqual(True, flag)

    def test_breachRule2_3b(self):
        # 3 connected by col
        solution = [[BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, SUN, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
                    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]
                    ]
        flag = main.breachRule2(solution)
        self.assertEqual(True, flag)

    def test_initASolution(self):
        main.initASolution()