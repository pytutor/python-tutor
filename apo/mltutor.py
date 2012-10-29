# -*- coding: utf-8 -*-
import sys, unittest

import matplotlib.pyplot as plt

from test_utils import MlTutorTestCase


def main():
    exercise, user_file = sys.argv[1:]
    ref_solution = exercise + '.py'
    test_file = exercise + '_tests.py'

    # Ensure that plt.show() doesn't actually do anything (it usually blocks)
    plt.show = lambda *args, **kwargs: None

    reference_solution = {}
    solution = {}
    execfile(ref_solution, {}, reference_solution)
    # destroy all figures so the user can't cheat and use the figures from our solution
    plt.close('all')
    execfile(user_file, {}, solution)

    # Ugly as hell, but easy :þ
    tests = {}
    execfile(test_file, tests)
    test_classes = [v for k,v in tests.items() if isinstance(v, type)
                    and issubclass(v, MlTutorTestCase)]

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for test_class in test_classes:
        # patch solution and reference solution on the testclass
        test_class.solution = solution
        test_class.reference_solution = reference_solution
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
