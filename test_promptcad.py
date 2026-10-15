import unittest
from promptcad import generate

class GenerateTests(unittest.TestCase):
    def test_box_dimensions(self):
        code = generate("box width 40 depth 20 height 8 mm")
        self.assertIn("cube([40, 20, 8]", code)
    def test_hollow_cylinder(self):
        code = generate("hollow cylinder radius 12 height 30 wall 2")
        self.assertIn("r=10", code)
        self.assertIn("h=30", code)
    def test_sphere(self):
        self.assertIn("sphere(r=5", generate("sphere radius 5"))
    def test_reject_invalid_wall(self):
        with self.assertRaises(ValueError): generate("tube radius 2 wall 2")

if __name__ == "__main__": unittest.main()
