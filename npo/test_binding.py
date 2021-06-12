from pathlib import Path

from lxml import etree

from npo.models import PageSearchResult

here = Path(__file__).parent.absolute()
schema_path = here.joinpath("schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd")


def test_bindings(xml_parser, xml_serializer, json_serializer):
    xml_fixture = here.joinpath("sample.xml")
    output = here.joinpath("sample.output.xml")
    ns_map = {
        "api": "urn:vpro:api:2013",
        "pages": "urn:vpro:pages:2013",
    }

    obj = xml_parser.from_path(xml_fixture, PageSearchResult)
    with output.open("w") as f:
        xml_serializer.write(f, obj, ns_map=ns_map)

    schema_doc = etree.parse(schema_path.as_uri())
    schema = etree.XMLSchema(schema_doc)
    output.with_suffix(".json").write_text(json_serializer.render(obj) + "\n")

    schema.assertValid(etree.parse(str(output)))

    assert obj.items.item[0].result.title == "Antibiotics"
