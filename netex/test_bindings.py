from pathlib import Path

import pytest
from lxml import etree

from netex.models import PublicationDelivery

here = Path(__file__).parent
output = here.joinpath("output")
functions = here.joinpath("NeTEx/examples/functions")
samples = [str(sample.relative_to(functions)) for sample in functions.rglob("*.xml")]
schema = here.joinpath("NeTEx/xsd/NeTEx_publication.xsd")

validator = etree.XMLSchema(etree.parse(str(schema)))


@pytest.mark.parametrize("sample", samples)
def test_bindings(sample, xml_parser, xml_serializer):

    obj = xml_parser.from_path(functions.joinpath(sample), PublicationDelivery)
    result = xml_serializer.render(obj, ns_map=xml_parser.ns_map)
    xml_parser.ns_map.clear()

    expected = output.joinpath(sample)
    if expected.exists():
        assert expected.read_text().strip() == result.strip()
    else:
        expected.parent.mkdir(parents=True, exist_ok=True)
        expected.write_text(result + "\n")

    validator.assertValid(etree.fromstring(result.encode()))
