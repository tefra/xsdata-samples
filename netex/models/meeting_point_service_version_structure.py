from dataclasses import dataclass, field
from typing import Optional
from netex.models.customer_service_version_structure import CustomerServiceVersionStructure
from netex.models.meeting_point_enumeration import MeetingPointEnumeration
from netex.models.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MeetingPointServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "MeetingPointService_VersionStructure"

    meeting_point_service_type: Optional[MeetingPointEnumeration] = field(
        default=None,
        metadata={
            "name": "MeetingPointServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
