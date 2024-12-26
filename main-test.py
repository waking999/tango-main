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

    def test_breachRule3_0(self):
        # right count of each character by row and col
        solution = [[SUN, SUN, MOON, MOON, SUN, MOON],
                    [SUN, SUN, MOON, MOON, SUN, MOON],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    [SUN, SUN, MOON, MOON, SUN, MOON],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    ]
        flag = main.breachRule3(solution)
        self.assertEqual(False, flag)


    def test_breachRule3_1(self):
        # wrong count of each character by row and col
        solution = [[SUN, MOON, MOON, MOON, SUN, MOON],
                    [SUN, SUN, MOON, MOON, SUN, MOON],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    [SUN, SUN, MOON, MOON, SUN, MOON],
                    [MOON, MOON, SUN, SUN, MOON, SUN],
                    ]
        flag = main.breachRule3(solution)
        self.assertEqual(True, flag)

    def test_breachRule3_2(self):
        # random solution
        solution = [[3, 1, 1, 3, 1, 3],
                    [3, 1, 1, 3, 1, 3],
                    [1, 1, 3, 3, 1, 3],
                    [3, 3, 1, 3, 1, 1],
                    [3, 1, 3, 3, 1, 1],
                    [1, 1, 3, 3, 1, 3]
                    ]
        flag = main.breachRule3(solution)
        self.assertEqual(True, flag)


    def test_is3Connected_0(self):
        # connected
        row=[3,2,4,0,1,5]
        flag=main.is3Connected(row)
        self.assertEqual(True, flag)

    def test_is3Connected_1(self):
        # connected
        row=[3,2,5,0,1,4]
        flag=main.is3Connected(row)
        self.assertEqual(False, flag)


    def test_produceASolution(self):
        main.produceASolution()

    # def test_initASolution(self):
    #     main.initASolution()

    def test_switchRowCol(self):
        origin = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
        expect = [[1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]
                ]

        actual=main.switchRowCol(origin)

        self.assertEqual(expect, actual)

    def test_provideClue(self):
        solution=main.initASolution()
        board =  [[BLANK] * cols for i in range(rows)]
        board, boardClickable, signPos= main.provideClue(solution,board)
        print(board)
        print(boardClickable)
        print(signPos)