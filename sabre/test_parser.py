import json
from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers import JsonSerializer

from sabre.models import OtaAirLowFareSearchRs

parser = XmlParser()
serializer = JsonSerializer(indent=2, dict_factory=DictFactory.FILTER_NONE)
cwd = Path(__file__).parent.absolute()


class ParserTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max_rs"
        xml_fixture = cwd.joinpath(f"{fixture}.xml")
        json_fixture = cwd.joinpath(f"{fixture}.json")

        obj = parser.from_path(xml_fixture, OtaAirLowFareSearchRs)

        expected = json_fixture.read_text()
        result = serializer.render(obj)

        self.assertEqual(json.loads(expected), json.loads(result))
        json_fixture.write_text(result + "\n")
