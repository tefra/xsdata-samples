from pathlib import Path

from lxml import etree

from travelport.models import LowFareSearchReq

cwd = Path(__file__).parent.absolute()
xsd_location = str(cwd.joinpath("schemas/air_v52_0/AirReqRsp.xsd"))


def test_bindings(json_parser, xml_serializer):
    fixture = "low_fare_search"
    json_fixture = cwd.joinpath(f"{fixture}.json")
    xml_fixture = cwd.joinpath(f"{fixture}.xml")

    obj = json_parser.from_path(json_fixture, LowFareSearchReq)
    json_parser.context.reset()

    xml = xml_serializer.render(
        obj=obj,
        ns_map={
            None: "http://www.travelport.com/schema/air_v52_0",
            "ns1": "http://www.travelport.com/schema/common_v52_0",
        },
    )

    xml_fixture.write_text(xml)

    schema = etree.XMLSchema(etree.parse(xsd_location))
    is_valid = schema.validate(etree.parse(str(xml_fixture)))
    assert is_valid, schema.error_log
