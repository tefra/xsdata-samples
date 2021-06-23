from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .alternative_texts_rel_structure import VersionedChildStructure
from .empty_type_2 import EmptyType2
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .line_in_direction_ref import LineInDirectionRef
from .lines_in_direction_refs_rel_structure import LinesInDirectionRefsRelStructure
from .operator_ref import OperatorRef
from .point_ref_structure import PointRefStructure
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_designator import ServiceDesignator
from .service_journey_ref_structure import ServiceJourneyRefStructure
from .stop_area_ref_structure import StopAreaRefStructure
from .stop_place_ref import StopPlaceRef
from .stop_place_ref_structure import StopPlaceRefStructure
from .time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleFilterVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "InterchangeRuleFilter_VersionedChildStructure"

    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
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
    all_lines_or_lines_in_direction_refs_or_line_in_direction_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllLines",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "linesInDirectionRefs",
                    "type": LinesInDirectionRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineInDirectionRef",
                    "type": LineInDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    adjacent_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "AdjacentPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: Optional[ServiceJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_designator: Optional[ServiceDesignator] = field(
        default=None,
        metadata={
            "name": "ServiceDesignator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_interchange_window: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumInterchangeWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
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
