from pathlib import Path

import pytest

from crossref.models.org.crossref.schema.pkg_5.pkg_3 import DoiBatch

here = Path(__file__).parent
examples = [
    "schema/examples/515151.xml",
    "schema/examples/525252.xml",
    "schema/test-examples/5.3.1-stm-asf.xml",
    "schema/test-examples/journal.article5.3.1.xml",
]
@pytest.mark.parametrize("example", examples)
def test_bindings(example, xml_parser, xml_serializer):
    example_path = here.joinpath(example)
    obj = xml_parser.from_path(example_path, DoiBatch)

    ns_map = {
        None: "http://www.crossref.org/schema/5.3.1",
        "ai": "http://www.crossref.org/AccessIndicators.xsd",
        "fr": "http://www.crossref.org/fundref.xsd",
    }
    result = xml_serializer.render(obj, ns_map=ns_map)

    output = here.joinpath("output").joinpath(example_path.name)
    if output.exists():
        assert output.read_text() == result
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result)
