from dataclasses import dataclass, field
from typing import Optional, Union

from .encumbrance_enumeration import EncumbranceEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .medical_need_enumeration import MedicalNeedEnumeration
from .mobility_enumeration import MobilityEnumeration
from .psychosensory_need_enumeration import PsychosensoryNeedEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserNeedVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "UserNeed_VersionedChildStructure"

    choice: Optional[
        Union[
            MobilityEnumeration,
            PsychosensoryNeedEnumeration,
            MedicalNeedEnumeration,
            EncumbranceEnumeration,
        ]
    ] = field(
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
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
