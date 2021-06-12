from pathlib import Path

from autosar.models import Autosar

cwd = Path(__file__).parent.absolute()


def test_ecu_example(xml_parser, xml_serializer):
    fixture = "MyECU.ecuc"
    xml_fixture = cwd.joinpath(f"{fixture}.arxml")
    xsdata_fixture = cwd.joinpath(f"{fixture}.xsdata.xml")

    obj = xml_parser.from_path(xml_fixture, Autosar)
    result = xml_serializer.render(obj)

    if xsdata_fixture.exists():
        expected = xsdata_fixture.read_text()
        assert expected == result
    else:
        xsdata_fixture.write_text(result)
