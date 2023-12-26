from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.delays import Delays
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.traffic_constriction_type_enum import (
    TrafficConstrictionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Impact:
    """
    An assessment of the impact that an event or operator action defined by the
    situation record has on the driving conditions.

    :ivar capacity_remaining: The ratio of current capacity to the
        normal (free flow) road capacity in the defined direction,
        expressed as a percentage. Capacity is the maximum number of
        vehicles that can pass a specified point on the road, in unit
        time given the specified conditions.
    :ivar number_of_lanes_restricted: The number of normally usable
        lanes on the carriageway which are now restricted either fully
        or partially (this may include the hard shoulder if it is
        normally available for operational use, e.g. in hard shoulder
        running schemes).
    :ivar number_of_operational_lanes: The number of usable lanes in the
        specified direction which remain fully operational (this may
        include the hard shoulder if it is being used as an operational
        lane).
    :ivar original_number_of_lanes: The normal number of usable lanes in
        the specified direction that the carriageway has before
        reduction due to roadworks or traffic events.
    :ivar residual_road_width: The total width of the combined
        operational lanes in the specified direction.
    :ivar traffic_constriction_type: The type of constriction to which
        traffic is subjected as a result of an event or operator action.
    :ivar delays:
    :ivar impact_extension:
    """

    capacity_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacityRemaining",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_lanes_restricted: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLanesRestricted",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_operational_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfOperationalLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    original_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    residual_road_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualRoadWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_constriction_type: Optional[TrafficConstrictionTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficConstrictionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    delays: Optional[Delays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    impact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "impactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
