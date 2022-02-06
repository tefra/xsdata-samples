from pathlib import Path

from bpmn.models import Definitions

cwd = Path(__file__).parent.absolute()


def test_waypoint_example(xml_parser, xml_serializer):
    fixture = "example"
    xml_fixture = cwd.joinpath(f"{fixture}.xml")
    xsdata_fixture = cwd.joinpath(f"{fixture}.xsdata.xml")

    obj = xml_parser.from_path(xml_fixture, Definitions)
    result = xml_serializer.render(obj, ns_map=xml_parser.ns_map)

    if xsdata_fixture.exists():
        expected = xsdata_fixture.read_text()
        assert expected == result
    else:
        xsdata_fixture.write_text(result)
