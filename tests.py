from unittest import TestCase

from main import phone_to_wame_link, phone_to_tme_link


class LinksTest(TestCase):
    def test_wame_links(self):
        expected = 'https://wa.me/77001234567'
        self.assertEqual(phone_to_wame_link('+77001234567'), expected)
        self.assertEqual(phone_to_wame_link('+7 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_wame_link('+7 (700) 123-4567'), expected)
        self.assertEqual(phone_to_wame_link('+7 (700) 1234567'), expected)
        self.assertEqual(phone_to_wame_link('+7 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_wame_link('8 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_wame_link('8 700 123-45-67'), expected)
        self.assertEqual(phone_to_wame_link('87001234567'), expected)
        self.assertEqual(phone_to_wame_link('7001234567'), expected)
        self.assertEqual(
            phone_to_wame_link('8 (999) 123-45-67'),
            'https://wa.me/79991234567',
        )

    def test_tme_links(self):
        expected = 'https://t.me/+77001234567'
        self.assertEqual(phone_to_tme_link('+77001234567'), expected)
        self.assertEqual(phone_to_tme_link('+7 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_tme_link('+7 (700) 123-4567'), expected)
        self.assertEqual(phone_to_tme_link('+7 (700) 1234567'), expected)
        self.assertEqual(phone_to_tme_link('+7 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_tme_link('8 (700) 123-45-67'), expected)
        self.assertEqual(phone_to_tme_link('8 700 123-45-67'), expected)
        self.assertEqual(phone_to_tme_link('87001234567'), expected)
        self.assertEqual(phone_to_tme_link('7001234567'), expected)
        self.assertEqual(
            phone_to_tme_link('8 (999) 123-45-67'),
            'https://t.me/+79991234567',
        )
