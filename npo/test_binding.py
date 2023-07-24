from pathlib import Path

from lxml import etree

from npo.models import PageSearchResult

here = Path(__file__).parent.absolute()
schema_path = here.joinpath("schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd")


def test_bindings(xml_parser, xml_serializer, json_serializer, code_serializer):
    xml_fixture = here.joinpath("sample.xml")
    output = here.joinpath("sample.output.xml")
    ns_map = {
        "api": "urn:vpro:api:2013",
        "pages": "urn:vpro:pages:2013",
    }

    obj = xml_parser.from_path(xml_fixture, PageSearchResult)
    result = xml_serializer.render(obj, ns_map=ns_map)
    code = code_serializer.render(obj)

    output.write_text(result)
    output.with_suffix(".py").write_text(code)
    output.with_suffix(".json").write_text(json_serializer.render(obj) + "\n")

    schema_doc = etree.parse(schema_path.as_uri())
    schema = etree.XMLSchema(schema_doc)
    schema.assertValid(etree.parse(str(output)))

    assert obj.items.item[0].result.title == "Antibiotics"
