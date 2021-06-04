from dataclasses import dataclass, field
from typing import Optional
from netex.models.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundTripVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RoundTrip_VersionStructure"

    trip_type: Optional[RoundTripTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    double_single_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoubleSingleFare",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_trip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShortTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
