from __future__ import annotations

from dataclasses import dataclass, field

from .round_trip_type_enumeration import RoundTripTypeEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundTripVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "RoundTrip_VersionStructure"

    trip_type: None | RoundTripTypeEnumeration = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    double_single_fare: None | bool = field(
        default=None,
        metadata={
            "name": "DoubleSingleFare",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_trip: None | bool = field(
        default=None,
        metadata={
            "name": "ShortTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_required: None | bool = field(
        default=None,
        metadata={
            "name": "IsRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
