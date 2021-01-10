from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from datexii.models import AlertCDirection
from datexii.models import AlertCDirectionEnum1
from datexii.models import AlertCDirectionEnum2
from datexii.models import AlertCLocation
from datexii.models import AlertCMethod4Linear
from datexii.models import AlertCMethod4PrimaryPointLocation
from datexii.models import AlertCMethod4SecondaryPointLocation
from datexii.models import LinearDirectionEnum1
from datexii.models import LinearDirectionEnum2
from datexii.models import OffsetDistance
from datexii.models import SingleRoadLinearLocation

config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=config)

here = Path(__file__).parent.absolute()
xsd_location = str(here.joinpath("schemas/DATEXII_3_D2Payload.xsd"))


class SerializerTests(TestCase):
    def test_manual_object(self):
        ns_map = {"loc": "http://datex2.eu/schema/3/locationReferencing"}

        primary_point = AlertCMethod4PrimaryPointLocation(
            alert_clocation=AlertCLocation(specific_location=10),
            offset_distance=OffsetDistance(offset_distance=2000),
        )
        secondary_point = AlertCMethod4SecondaryPointLocation(
            alert_clocation=AlertCLocation(specific_location=12),
            offset_distance=OffsetDistance(offset_distance=150),
        )
        obj = SingleRoadLinearLocation(
            alert_clinear=AlertCMethod4Linear(
                alert_clocation_country_code="F",
                alert_clocation_table_number=32,
                alert_clocation_table_version="1.0",
                alert_cdirection=AlertCDirection(
                    alert_cdirection_coded=AlertCDirectionEnum2(
                        value=AlertCDirectionEnum1.NEGATIVE
                    ),
                    alert_caffected_direction=LinearDirectionEnum2(
                        value=LinearDirectionEnum1.OPPOSITE
                    ),
                ),
                alert_cmethod4_primary_point_location=primary_point,
                alert_cmethod4_secondary_point_location=secondary_point,
            )
        )

        result = serializer.render(obj, ns_map=ns_map)
        output = here.joinpath("sample.output.xml")
        if output.exists():
            self.assertEqual(output.read_text(), result)
        else:
            output.write_text(result)
