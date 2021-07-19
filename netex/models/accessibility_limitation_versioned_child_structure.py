from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .limitation_status_enumeration import LimitationStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityLimitationVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessibilityLimitation_VersionedChildStructure"

    wheelchair_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    step_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lift_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audible_signals_available: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_signs_available: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
