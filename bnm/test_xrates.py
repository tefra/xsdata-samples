from pathlib import Path
from unittest import mock
from unittest import TestCase

from requests import Response

from bnm.xrates import Currencies
from bnm.xrates import Currency
from bnm.xrates import fetch


class FetchTest(TestCase):
    @mock.patch("bnm.xrates.requests.get")
    def test_parser(self, mock_requests_get):
        response = Response()
        response.status_code = 200

        sample_xml = Path(__file__).with_name("sample.xml").read_text()
        type(response).text = mock.PropertyMock(return_value=sample_xml)  # type: ignore
        mock_requests_get.return_value = response
        currencies = fetch()

        self.assertEqual("Official exchange rate", currencies.name)
        self.assertEqual("19.04.2020", currencies.date)
        self.assertEqual(42, len(currencies.values))
        self.assertIsInstance(currencies, Currencies)
        self.assertIsInstance(currencies.values[0], Currency)
