from dataclasses import dataclass, field
from typing import Optional
from .derived_view_structure import DerivedViewStructure
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .multilingual_string import MultilingualString
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .quay_ref_structure import QuayRefStructure
from .stop_place_ref import StopPlaceRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerStopAssignmentDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PassengerStopAssignment_DerivedViewStructure"

    vehicle_journey_stop_assignment_ref: Optional[VehicleJourneyStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic_stop_assignment_ref: Optional[DynamicStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "DynamicStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_stop_assignment_ref: Optional[PassengerStopAssignmentRef] = field(
        default=None,
        metadata={
            "name": "PassengerStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_ref: Optional[StopPlaceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_ref: Optional[QuayRefStructure] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "QuayName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
