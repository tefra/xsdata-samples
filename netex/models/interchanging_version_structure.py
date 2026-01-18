from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .register_break_of_journey_enumeration import (
    RegisterBreakOfJourneyEnumeration,
)
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Interchanging_VersionStructure"

    can_interchange: bool | None = field(
        default=None,
        metadata={
            "name": "CanInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "FromMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "ToMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_interchanges: int | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfInterchanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_time_to_make_atransfer: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumTimeToMakeATransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_break_journey: bool | None = field(
        default=None,
        metadata={
            "name": "CanBreakJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_border: bool | None = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    register_break_of_journey: RegisterBreakOfJourneyEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "RegisterBreakOfJourney",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
