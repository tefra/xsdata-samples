import json
from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import DictSerializer

from samples.amadeus.output.fare_master_pricer_travel_board_search_reply_15_3_1_a import (
    FareMasterPricerTravelBoardSearchReply,
)

parser = XmlParser()
serializer = DictSerializer()
dir = Path(__file__).parent.absolute()


def value_dict(data):
    return {x: v for x, v in dict(data).items() if v is not None}


class ParserTests(TestCase):
    def test_master_pricer(self):
        fixture = "master_pricer_rs"

        xml_str = dir.joinpath(f"{fixture}.xml")
        obj = parser.from_path(xml_str, FareMasterPricerTravelBoardSearchReply)

        output = dir.joinpath(f"{fixture}.json")
        expected = json.loads(output.read_text())

        result = serializer.render(obj, dict_factory=serializer.filter_none)
        self.assertEqual(expected, result)
        output.write_text(json.dumps(result, indent=2))
