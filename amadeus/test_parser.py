import json
from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers import JsonSerializer

from amadeus.models.response import FareMasterPricerTravelBoardSearchReply

parser = XmlParser()
serializer = JsonSerializer(indent=2, dict_factory=DictFactory.FILTER_NONE)
cwd = Path(__file__).parent.absolute()


def value_dict(data):
    return {x: v for x, v in dict(data).items() if v is not None}


class ParserTests(TestCase):
    def test_master_pricer(self):
        fixture = "master_pricer_rs"
        xml_fixture = cwd.joinpath(f"{fixture}.xml")
        json_fixture = cwd.joinpath(f"{fixture}.json")

        obj = parser.from_path(xml_fixture, FareMasterPricerTravelBoardSearchReply)

        expected = json_fixture.read_text()
        result = serializer.render(obj)

        self.assertEqual(json.loads(expected), json.loads(result))
        json_fixture.write_text(result)
