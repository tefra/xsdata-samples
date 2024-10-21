from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .crossing_equipment import CrossingEquipment
from .entrance_equipment import EntranceEquipment
from .escalator_equipment import EscalatorEquipment
from .general_sign_structure import GeneralSignStructure
from .heading_sign_structure import HeadingSignStructure
from .help_point_equipment import HelpPointEquipment
from .lift_call_equipment import LiftCallEquipment
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

    choice: Iterable[
        Union[
            OtherPlaceEquipment,
            RoughSurface,
            EntranceEquipment,
            StaircaseEquipment,
            LiftEquipment,
            LiftCallEquipment,
            EscalatorEquipment,
            TravelatorEquipment,
            RampEquipment,
            QueueingEquipment,
            CrossingEquipment,
            PlaceLighting,
            PlaceSignStructure,
            HeadingSignStructure,
            GeneralSignStructure,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            RubbishDisposalEquipment,
            SanitaryEquipment,
            TicketingEquipment,
            TicketValidatorEquipment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherPlaceEquipment",
                    "type": OtherPlaceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftCallEquipment",
                    "type": LiftCallEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
