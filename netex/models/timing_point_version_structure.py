from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.models.point_version_structure import PointVersionStructure
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointVersionStructure(PointVersionStructure):
    class Meta:
        name = "TimingPoint_VersionStructure"

    timing_point_status: Optional[TimingPointStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_for_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AllowedForWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
