from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .entrance_equipment import EntranceEquipment
from .escalator_equipment import EscalatorEquipment
from .general_sign_structure import GeneralSignStructure
from .heading_sign_structure import HeadingSignStructure
from .help_point_equipment import HelpPointEquipment
from .lift_equipment import LiftEquipment
from .other_place_equipment import OtherPlaceEquipment
from .passenger_safety_equipment import PassengerSafetyEquipment
from .place_lighting import PlaceLighting
from .place_sign_structure import PlaceSignStructure
from .queueing_equipment import QueueingEquipment
from .ramp_equipment import RampEquipment
from .rough_surface import RoughSurface
from .rubbish_disposal_equipment import RubbishDisposalEquipment
from .sanitary_equipment import SanitaryEquipment
from .staircase_equipment import StaircaseEquipment
from .ticket_validator_equipment import TicketValidatorEquipment
from .ticketing_equipment import TicketingEquipment
from .travelator_equipment import TravelatorEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExplicitPlaceEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "explicitPlaceEquipments_RelStructure"

    other_place_equipment: List[OtherPlaceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "OtherPlaceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rough_surface: List[RoughSurface] = field(
        default_factory=list,
        metadata={
            "name": "RoughSurface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_equipment: List[EntranceEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EntranceEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staircase_equipment: List[StaircaseEquipment] = field(
        default_factory=list,
        metadata={
            "name": "StaircaseEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lift_equipment: List[LiftEquipment] = field(
        default_factory=list,
        metadata={
            "name": "LiftEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_equipment: List[EscalatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "EscalatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travelator_equipment: List[TravelatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TravelatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ramp_equipment: List[RampEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RampEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queueing_equipment: List[QueueingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "QueueingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crossing_equipment: List[CrossingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "CrossingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_lighting: List[PlaceLighting] = field(
        default_factory=list,
        metadata={
            "name": "PlaceLighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_sign: List[PlaceSignStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    heading_sign: List[HeadingSignStructure] = field(
        default_factory=list,
        metadata={
            "name": "HeadingSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_sign: List[GeneralSignStructure] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    help_point_equipment: List[HelpPointEquipment] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_safety_equipment: List[PassengerSafetyEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rubbish_disposal_equipment: List[RubbishDisposalEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_equipment: List[SanitaryEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_equipment: List[TicketingEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketingEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticket_validator_equipment: List[TicketValidatorEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
