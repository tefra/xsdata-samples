from dataclasses import dataclass, field
from typing import Optional
from netex.models.booking_arrangements_structure import BookingArrangementsStructure
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CancellingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Cancelling_VersionStructure"

    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
