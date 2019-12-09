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
dir = Path(__file__).parent.absolute()
xsd_location = str(
    dir.joinpath(
        "../../xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd"
    )
)


class SerializerTests(TestCase):
    def test_master_pricer(self):
        fixture = "master_pricer_rq"

        json_data = dir.joinpath(f"{fixture}.json").read_text()
        xml = serializer.render(
            obj=parser.from_json(json_data, FareMasterPricerTravelBoardSearch),
            pretty_print=True,
        )

        output = dir.joinpath(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
