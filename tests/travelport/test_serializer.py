from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import DictParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from samples.travelport.output.air_v48_0.air_req_rsp import LowFareSearchReq

parser = DictParser()
serializer = XmlSerializer()
dir = Path(__file__).parent.absolute()
xsd_location = str(
    dir.joinpath("../../xsd/travelport/air_v48_0/AirReqRsp.xsd")
)


class SerializerTests(TestCase):
    def test_low_fare_search(self):
        fixture = "low_fare_search"

        json_data = dir.joinpath(f"{fixture}.json").read_text()
        xml = serializer.render(
            obj=parser.from_json(json_data, LowFareSearchReq),
            pretty_print=True,
        )

        output = dir.joinpath(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
