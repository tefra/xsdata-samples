from pathlib import Path
from typing import Dict

import pytest
from lxml import etree

from sdmx_ml.models import *  # noqa

here = Path(__file__).parent
output = here.joinpath("output")
samples_dir = here.joinpath("repo/samples")
samples = [
    str(sample.relative_to(samples_dir)) for sample in samples_dir.rglob("*.xml")
]
schema = here.joinpath("repo/schemas/SDMXMessage.xsd")

validator = etree.XMLSchema(etree.parse(str(schema)))


@pytest.mark.parametrize("sample", samples)
def test_bindings(sample, xml_parser, xml_serializer, code_serializer):
    ns_map: Dict = {}
    sample_xml = samples_dir.joinpath(sample).read_bytes()
    obj = xml_parser.from_bytes(sample_xml)
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
    except Exception:
        if validator.validate(etree.fromstring(sample_xml)):
            raise

        pytest.skip(f"Original xml fails validation: {sample}")
