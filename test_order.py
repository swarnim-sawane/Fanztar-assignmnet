
import unittest
from order import process_order

class TestOrderProcessing(unittest.TestCase):
    def test_process_order(self):
        components = ["I", "A", "D", "F", "K"]
        parts, total = process_order(components)
        self.assertEqual(parts, ["Android OS", "LED Screen", "Wide-Angle Camera", "USB-C Port", "Metallic Body"])
        self.assertAlmostEqual(total, 142.3, places=2)

if __name__ == '__main__':
    unittest.main()
