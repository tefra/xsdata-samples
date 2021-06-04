from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.empty_type_2 import EmptyType2
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.journey_designator import JourneyDesignator
from netex.models.line_in_direction_ref import LineInDirectionRef
from netex.models.lines_in_direction_refs_rel_structure import LinesInDirectionRefsRelStructure
from netex.models.operator_ref import OperatorRef
from netex.models.point_ref_structure import PointRefStructure
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.service_designator import ServiceDesignator
from netex.models.service_journey_ref_structure import ServiceJourneyRefStructure
from netex.models.stop_area_ref_structure import StopAreaRefStructure
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_place_ref_structure import StopPlaceRefStructure
from netex.models.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleParameterStructure:
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
    all_lines: Optional[EmptyType2] = field(
        default=None,
        metadata={
            "name": "AllLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lines_in_direction_refs: Optional[LinesInDirectionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "linesInDirectionRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_in_direction_ref: List[LineInDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineInDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
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
    journey_designator: Optional[JourneyDesignator] = field(
        default=None,
        metadata={
            "name": "JourneyDesignator",
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
