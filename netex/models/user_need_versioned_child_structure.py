from __future__ import annotations

from dataclasses import dataclass, field

from .encumbrance_enumeration import EncumbranceEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .medical_need_enumeration import MedicalNeedEnumeration
from .mobility_enumeration import MobilityEnumeration
from .psychosensory_need_enumeration import PsychosensoryNeedEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserNeedVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "UserNeed_VersionedChildStructure"

    choice: (
        None
        | MobilityEnumeration
        | PsychosensoryNeedEnumeration
        | MedicalNeedEnumeration
        | EncumbranceEnumeration
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityNeed",
                    "type": MobilityEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PsychosensoryNeed",
                    "type": PsychosensoryNeedEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MedicalNeed",
                    "type": MedicalNeedEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EncumbranceNeed",
                    "type": EncumbranceEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    excluded: None | bool = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    need_ranking: None | int = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
