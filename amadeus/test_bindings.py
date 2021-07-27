import json
from pathlib import Path

from lxml import etree

from amadeus.models import FareMasterPricerTravelBoardSearch
from amadeus.models import FareMasterPricerTravelBoardSearchReply

cwd = Path(__file__).parent.absolute()
xsd_location = str(
    cwd.joinpath("schemas/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd")
)


def value_dict(data):
    return {x: v for x, v in dict(data).items() if v is not None}


def test_serializing(json_parser, xml_serializer):
    fixture = "master_pricer_rq"
    json_fixture = cwd.joinpath(f"{fixture}.json")
    xml_fixture = cwd.joinpath(f"{fixture}.xml")

    obj = json_parser.from_path(json_fixture, FareMasterPricerTravelBoardSearch)

    json_parser.context.reset()

    xml = xml_serializer.render(
        obj=obj, ns_map={None: "http://xml.amadeus.com/FMPTBQ_15_3_1A"}
    )

    xml_fixture.write_text(xml)

    schema = etree.XMLSchema(etree.parse(xsd_location))
    is_valid = schema.validate(etree.parse(str(xml_fixture)))
    assert is_valid, schema.error_log


def test_parsing(xml_parser, json_serializer):
    fixture = "master_pricer_rs"
    xml_fixture = cwd.joinpath(f"{fixture}.xml")
    json_fixture = cwd.joinpath(f"{fixture}.json")

    obj = xml_parser.from_path(xml_fixture, FareMasterPricerTravelBoardSearchReply)

    expected = json_fixture.read_text()
    json_serializer.dict_factory = value_dict
    result = json_serializer.render(obj)

    assert json.loads(expected) == json.loads(result)
    json_fixture.write_text(result + "\n")
