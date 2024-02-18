from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .audible_signals_available import AudibleSignalsAvailable
from .escalator_free_access import EscalatorFreeAccess
from .lift_free_access import LiftFreeAccess
from .step_free_access import StepFreeAccess
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
