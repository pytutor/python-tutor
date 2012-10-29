import unittest

import numpy as np


class TestGeneratorMeta(type):
    def __new__(mcl, classname, bases, classdict):
        newdict = classdict.copy()
        assert_equal = classdict.get('assert_equal', [])

        for variable in assert_equal:

            def test_equality(self, variable=variable):
                self.assertIn(variable, self.solution)
                sol = self.solution[variable]
                ref = self.reference_solution[variable]
                if all(map(lambda x: isinstance(x, np.ndarray), (sol, ref))):
                    self.assertTrue(np.equal(ref, sol).all())
                else:
                    self.assertEqual(sol, ref)

            newdict['test_equality_%s' % (variable,)] = test_equality

        return super(TestGeneratorMeta, mcl).__new__(mcl, classname, bases,
            newdict)


class MlTutorTestCase(unittest.TestCase):
    __metaclass__ = TestGeneratorMeta

