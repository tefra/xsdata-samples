from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dict.parser import DictParser
from xsdata.formats.xml.serializer import XmlSerializer

from samples.amadeus.output.fare_master_pricer_travel_board_search_15_3_1_a import (
    FareMasterPricerTravelBoardSearch,
)

parser = DictParser()
serializer = XmlSerializer()


class SerializerTests(TestCase):
    def test_master_pricer(self):
        fixture = "master_pricer"
        xsd = (
            "../../xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd"
        )

        json_data = Path(f"{fixture}.json").read_text()
        obj = parser.from_json(json_data, FareMasterPricerTravelBoardSearch)

        xml = serializer.render(obj, pretty_print=True)

        output = Path(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd))
        self.assertTrue(schema.validate(etree.parse(str(output))))
