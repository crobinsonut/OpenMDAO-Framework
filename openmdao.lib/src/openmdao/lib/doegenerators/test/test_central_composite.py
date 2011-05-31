"""
Test CentralComposite.
"""

# pylint: disable-msg=C0111,C0103

import unittest

from openmdao.lib.doegenerators.central_composite import CentralComposite

class TestCase(unittest.TestCase):
    
    def setup(self):
        pass
    
    def teardown(self):
        pass
    
    def test_face_centered(self): 
        
        fcc = CentralComposite(type="Face-Centered", alpha=0.8, center_points=1)
        fcc.num_parameters = 2
        cases = [case for case in fcc]
        expected = [(0.0,0.0),(0.0,1.0),(1.0,0.0),(1.0,1.0),(0.0,0.5),(0.5,0.0),(0.5,1.0),(1.0,0.5),[0.5,0.5]]
        self.assertEqual(expected,cases)

    def test_user_defined(self):
        ccc = CentralComposite(type="Spherical", alpha=0.8, center_points=1)
        ccc.num_parameters = 2
        cases = [case for case in ccc]
        expected = [(0,0),(0,1),(1,0),(1,1),(0.5,0.1),(0.1,0.5),(0.9,0.5),(0.5,0.9),[0.5,0.5]]
        # self.assertEqual(expected,cases)
        
        for case,expected in zip(cases,expected): 
            self.assertAlmostEquals(case[0],expected[0],8)
            self.assertAlmostEquals(case[1],expected[1],8)

    def test_rotatable(self):
        ccc = CentralComposite(type="Spherical", alpha=None, center_points=1)
        ccc.num_parameters = 2
        cases = [case for case in ccc]
        expected = [(0.146446609406726,0.146446609406726),(0.853553390593274,0.146446609406726),(0.853553390593274,0.853553390593274),(0.146446609406726,0.853553390593274),(0.5,0),(1,0.5),(0.5,1),(0,0.5),[0.5,0.5]]
        for case,expected in zip(cases,expected): 
            self.assertAlmostEquals(case[0],expected[0],8)
            self.assertAlmostEquals(case[1],expected[1],8)

if __name__ == "__main__":
    unittest.main()
