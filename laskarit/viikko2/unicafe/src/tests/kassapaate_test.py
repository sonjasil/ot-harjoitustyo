import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luvut_ovat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lounaiden_osto_toimii_kateisella(self):
        if self.kassapaate.syo_edullisesti_kateisella(250):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
            self.assertEqual(self.kassapaate.edulliset, 1)
        if self.kassapaate.syo_maukkaasti_kateisella(450):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
            self.assertEqual(self.kassapaate.maukkaat, 1)
        if self.kassapaate.syo_edullisesti_kateisella(230):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
            self.assertEqual(self.kassapaate.edulliset, 1)
        if self.kassapaate.syo_maukkaasti_kateisella(300):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
            self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        kortti1 = Maksukortti(1000)
        kortti2 = Maksukortti(200)
        if self.kassapaate.syo_edullisesti_kortilla(kortti1):
            self.assertEqual(self.kassapaate.edulliset, 1)
            self.assertEqual(str(kortti1), "Kortilla on rahaa 7.60 euroa")
        if self.kassapaate.syo_maukkaasti_kortilla(kortti1):
            self.assertEqual(self.kassapaate.maukkaat, 1)
            self.assertEqual(str(kortti1), "Kortilla on rahaa 3.60 euroa")
        if self.kassapaate.syo_edullisesti_kortilla(kortti2):
            self.assertEqual(self.kassapaate.edulliset, 0)
            self.assertEqual(str(kortti1), "Kortilla on rahaa 2.00 euroa")
        if self.kassapaate.syo_maukkaasti_kortilla(kortti2):
            self.assertEqual(self.kassapaate.maukkaat, 0)
            self.assertEqual(str(kortti1), "Kortilla on rahaa 2.00 euroa")

    def test_rahan_lataus_kortille_toimii(self):
        kortti = Maksukortti(1000)

        if self.kassapaate.lataa_rahaa_kortille(kortti, 200):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
            self.assertEqual(str(kortti), "Kortilla on rahaa 12.00 euroa")
        if self.kassapaate.lataa_rahaa_kortille(kortti, -200):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
            self.assertEqual(str(kortti), "Kortilla on rahaa 12.00 euroa")
        