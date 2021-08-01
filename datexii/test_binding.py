from pathlib import Path

from lxml import etree

from datexii.models.eu.datexii.v2 import D2LogicalModel

here = Path(__file__).parent.absolute()
xsd_location = str(here.joinpath("schemas/DATEXIISchema_2_2_3.xsd"))


def test_bindings(xml_parser, xml_serializer):
    ns_map = {None: "http://datex2.eu/schema/2/2_0"}
    sample = here.joinpath("sample.xml")

    payload = xml_parser.from_path(sample, D2LogicalModel)
    result = xml_serializer.render(payload, ns_map=ns_map)

    output = here.joinpath("sample.xsdata.xml")
    if output.exists():
        assert output.read_text() == result
    else:
        output.write_text(result)

    schema = etree.XMLSchema(etree.parse(xsd_location))
    is_valid = schema.validate(etree.parse(str(output)))
    assert is_valid, schema.error_log
