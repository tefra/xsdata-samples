from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .empty_type_2 import EmptyType2
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .journey_designator import JourneyDesignator
from .line_in_direction_ref import LineInDirectionRef
from .lines_in_direction_refs_rel_structure import (
    LinesInDirectionRefsRelStructure,
)
from .operator_ref import OperatorRef
from .point_ref_structure import PointRefStructure
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_designator import ServiceDesignator
from .service_journey_ref_structure import ServiceJourneyRefStructure
from .stop_area_ref_structure import StopAreaRefStructure
from .stop_place_ref import StopPlaceRef
from .stop_place_ref_structure import StopPlaceRefStructure
from .taxi_rank_ref import TaxiRankRef
from .time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleParameterStructure:
    transport_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref: OperatorRef | None = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_area_ref: StopAreaRefStructure | None = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_ref: TaxiRankRef | StopPlaceRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    all_lines_or_lines_in_direction_refs_or_line_in_direction_ref: Iterable[
        EmptyType2 | LinesInDirectionRefsRelStructure | LineInDirectionRef
    ] = field(
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
        },
    )
    scheduled_stop_point_ref: (
        FareScheduledStopPointRef | ScheduledStopPointRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    adjacent_stop_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "AdjacentStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_stop_place_ref: StopPlaceRefStructure | None = field(
        default=None,
        metadata={
            "name": "AdjacentStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "AdjacentPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_stop_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref: TimeDemandTypeRef | None = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_journey_ref_or_journey_designator_or_service_designator: (
        ServiceJourneyRefStructure
        | JourneyDesignator
        | ServiceDesignator
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyDesignator",
                    "type": JourneyDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceDesignator",
                    "type": ServiceDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_interchange_window: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumInterchangeWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
