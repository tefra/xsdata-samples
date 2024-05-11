from dataclasses import dataclass, field
from typing import Optional

from .audible_signals_available import AudibleSignalsAvailable
from .entity_in_version_structure import VersionedChildStructure
from .escalator_free_access import EscalatorFreeAccess
from .guide_dog_access import GuideDogAccess
from .level_access_into_vehicle import LevelAccessIntoVehicle
from .lift_free_access import LiftFreeAccess
from .ramp_free_access import RampFreeAccess
from .stair_free_access import StairFreeAccess
from .step_free_access import StepFreeAccess
from .tactile_guidance_available import TactileGuidanceAvailable
from .visual_signs_available import VisualSignsAvailable
from .wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityLimitationVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessibilityLimitation_VersionedChildStructure"

    wheelchair_access: Optional[WheelchairAccess] = field(
        default=None,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    step_free_access: Optional[StepFreeAccess] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stair_free_access: Optional[StairFreeAccess] = field(
        default=None,
        metadata={
            "name": "StairFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    escalator_free_access: Optional[EscalatorFreeAccess] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lift_free_access: Optional[LiftFreeAccess] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ramp_free_access: Optional[RampFreeAccess] = field(
        default=None,
        metadata={
            "name": "RampFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    level_access_into_vehicle: Optional[LevelAccessIntoVehicle] = field(
        default=None,
        metadata={
            "name": "LevelAccessIntoVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audible_signals_available: Optional[AudibleSignalsAvailable] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_signs_available: Optional[VisualSignsAvailable] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guidance_available: Optional[TactileGuidanceAvailable] = field(
        default=None,
        metadata={
            "name": "TactileGuidanceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    guide_dog_access: Optional[GuideDogAccess] = field(
        default=None,
        metadata={
            "name": "GuideDogAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
