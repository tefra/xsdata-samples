from pathlib import Path
from typing import Dict

import pytest
from lxml import etree
from lxml.etree import DocumentInvalid

from ipxact.models import *  # noqa

here = Path(__file__).parent
output = here.joinpath("output")
examples = here.joinpath("examples")

samples = [str(sample.relative_to(examples)) for sample in examples.rglob("*.xml")]
schema = here.joinpath("schemas/index.xsd")

validator = etree.XMLSchema(etree.parse(str(schema)))


@pytest.mark.parametrize("sample", samples)
def test_bindings(sample, xml_parser, xml_serializer, code_serializer):
    ns_map: Dict = {}
    obj = xml_parser.from_path(examples.joinpath(sample), ns_map=ns_map)
    result = xml_serializer.render(obj, ns_map=ns_map)
    code = code_serializer.render(obj)

    expected = output.joinpath(sample)
    expected.parent.mkdir(parents=True, exist_ok=True)
    expected.with_suffix(".py").write_text(code)

    if expected.exists():
        assert expected.read_text().strip() == result.strip()
    else:
        expected.write_text(result + "\n")

    try:
        validator.assertValid(etree.fromstring(result.encode()))
    except DocumentInvalid:
        if not validator.validate(etree.parse(examples.joinpath(sample))):
            pytest.skip("Failed original.")
        else:
            raise
