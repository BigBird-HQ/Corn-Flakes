import unittest

from back_to_sender_logistics import logistics


class MyTestCase(unittest.TestCase):
    def test_that_dispatch_rider_made_less_than_50_daily_collection_successful_delivery(self):
        # logistics = Logistics()
        logistics.calculate_daily_pay(40)
        self.assertEqual(11400, logistics.calculate_daily_pay(40))

    def test_that_dispatch_rider_made_less_than_60_daily_collection_successful_delivery(self):
        # logistics = Logistics()
        logistics.calculate_daily_pay(55)
        self.assertEqual(16000, logistics.calculate_daily_pay(55))

    def test_that_dispatch_rider_made_less_than_70_daily_collection_successful_delivery(self):
        # logistics = Logistics()
        logistics.calculate_daily_pay(67)
        self.assertEqual(21750, logistics.calculate_daily_pay(67))

    def test_that_dispatch_rider_made_more_than_70_daily_collection_successful_delivery(self):
        # logistics = Logistics()
        logistics.calculate_daily_pay(80)
        self.assertEqual(45000, logistics.calculate_daily_pay(80))


if __name__ == '__main__':
    unittest.main()
