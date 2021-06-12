import json
from pathlib import Path

from lxml import etree
from xsdata.formats.dataclass.serializers import DictFactory

from sabre.models import OtaAirLowFareSearchRq
from sabre.models import OtaAirLowFareSearchRs

cwd = Path(__file__).parent.absolute()
xsd_location = str(cwd.joinpath("schemas/BargainFinderMaxRQ_v1-9-7.xsd"))


def test_serializing(json_parser, xml_serializer):

    fixture = "bargain_finder_max_rq"
    json_fixture = cwd.joinpath(f"{fixture}.json")
    xml_fixture = cwd.joinpath(f"{fixture}.xml")

    obj = json_parser.from_path(json_fixture, OtaAirLowFareSearchRq)
    json_parser.context.reset()
    xml = xml_serializer.render(
        obj, ns_map={None: "http://www.opentravel.org/OTA/2003/05"}
    )

    xml_fixture.write_text(xml)

    schema = etree.XMLSchema(etree.parse(xsd_location))
    is_valid = schema.validate(etree.parse(str(xml_fixture)))

    assert is_valid, schema.error_log


def test_parsing(xml_parser, json_serializer):
    json_serializer.dict_factory = DictFactory.FILTER_NONE

    fixture = "bargain_finder_max_rs"
    xml_fixture = cwd.joinpath(f"{fixture}.xml")
    json_fixture = cwd.joinpath(f"{fixture}.json")

    obj = xml_parser.from_path(xml_fixture, OtaAirLowFareSearchRs)
    result = json_serializer.render(obj)

    if json_fixture.exists():
        expected = json_fixture.read_text()
        assert json.loads(expected) == json.loads(result)
    else:
        json_fixture.write_text(result + "\n")
