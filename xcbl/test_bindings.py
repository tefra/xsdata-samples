from pathlib import Path
from typing import Dict

import pytest
from lxml import etree

from xcbl.models import *  # noqa

here = Path(__file__).parent
schemas = here.joinpath("schemas")
output_dir = here.joinpath("output")
samples_dir = here.joinpath("samples")
samples = list(map(str, samples_dir.rglob("*.xml")))


@pytest.mark.parametrize("sample", samples)
def test_bindings(sample, xml_parser, xml_serializer):
    ns_map: Dict = {}
    obj = xml_parser.parse(sample, ns_map=ns_map)
    result = xml_serializer.render(obj, ns_map=ns_map)

    sample_path = Path(sample).relative_to(samples_dir)
    expected = output_dir.joinpath(sample_path)
    if expected.exists():
        assert expected.read_text().strip() == result.strip()
    else:
        expected.parent.mkdir(parents=True, exist_ok=True)
        expected.write_text(result + "\n")

    root = etree.XML(result.encode())

    dtd = etree.DTD(schemas.joinpath(root.tag + ".dtd"))
    dtd.assertValid(root)

    # validator.assertValid(etree.fromstring(result.encode()))
