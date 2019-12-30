from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from samples.amadeus.output.fare_master_pricer_travel_board_search_15_3_1_a import (
    FareMasterPricerTravelBoardSearch,
)

parser = JsonParser()
serializer = XmlSerializer(pretty_print=True)
cwd = Path(__file__).parent.absolute()
xsd_location = str(
    cwd.joinpath(
        "../../xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd"
    )
)


class SerializerTests(TestCase):
    def test_master_pricer(self):
        fixture = "master_pricer_rq"
        json_fixture = cwd.joinpath(f"{fixture}.json")
        xml_fixture = cwd.joinpath(f"{fixture}.xml")

        obj = parser.from_path(json_fixture, FareMasterPricerTravelBoardSearch)
        xml = serializer.render(obj=obj)

        xml_fixture.write_text(xml)

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(xml_fixture)))
        self.assertTrue(is_valid, schema.error_log)
