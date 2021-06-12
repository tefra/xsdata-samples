from pathlib import Path

from lxml import etree

from reqif.models import ReqIf

here = Path(__file__).parent.absolute()


def test_bindings(xml_parser, xml_serializer, json_serializer):
    xml_fixture = here.joinpath("sample.xml")
    output = here.joinpath("sample.output.xml")

    obj = xml_parser.from_path(xml_fixture, ReqIf)
    ns_map = {
        None: "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        "xhtml": "http://www.w3.org/1999/xhtml",
    }

    xml_serializer.config.encoding = "ascii"
    with output.open("w") as f:
        xml_serializer.write(f, obj, ns_map=ns_map)

    schema_doc = etree.parse(here.joinpath("schemas/reqif.xsd").as_uri())
    schema = etree.XMLSchema(schema_doc)
    output.with_suffix(".json").write_text(json_serializer.render(obj) + "\n")

    schema.assertValid(etree.parse(str(output)))
