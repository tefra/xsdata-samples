from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from samples.travelport.output.air_v48_0.air_req_rsp import LowFareSearchReq

parser = JsonParser()
serializer = XmlSerializer(pretty_print=True)
cwd = Path(__file__).parent.absolute()
xsd_location = str(
    cwd.joinpath("../../xsd/travelport/air_v48_0/AirReqRsp.xsd")
)


class SerializerTests(TestCase):
    def test_low_fare_search(self):
        fixture = "low_fare_search"
        json_fixture = cwd.joinpath(f"{fixture}.json")
        xml_fixture = cwd.joinpath(f"{fixture}.xml")

        obj = parser.from_path(json_fixture, LowFareSearchReq)
        xml = serializer.render(obj=obj)

        xml_fixture.write_text(xml)

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(xml_fixture)))
        self.assertTrue(is_valid, schema.error_log)
