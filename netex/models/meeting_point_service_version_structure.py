from __future__ import annotations

from dataclasses import dataclass, field

from .customer_service_version_structure import CustomerServiceVersionStructure
from .meeting_point_enumeration import MeetingPointEnumeration
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MeetingPointServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "MeetingPointService_VersionStructure"

    meeting_point_service_type: MeetingPointEnumeration | None = field(
        default=None,
        metadata={
            "name": "MeetingPointServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
