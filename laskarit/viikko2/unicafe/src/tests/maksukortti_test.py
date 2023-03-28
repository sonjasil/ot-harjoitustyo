import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_asetettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(300)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 13.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        if self.maksukortti.ota_rahaa(300):
            self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")
        if self.maksukortti.ota_rahaa(11000):
            self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
            