from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .encumbrance_enumeration import EncumbranceEnumeration
from .medical_need_enumeration import MedicalNeedEnumeration
from .mobility_enumeration import MobilityEnumeration
from .pyschosensory_need_enumeration import PyschosensoryNeedEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserNeedVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "UserNeed_VersionedChildStructure"

    mobility_need: Optional[MobilityEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityNeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    psychosensory_need: Optional[PyschosensoryNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "PsychosensoryNeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    medical_need: Optional[MedicalNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "MedicalNeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    encumbrance_need: Optional[EncumbranceEnumeration] = field(
        default=None,
        metadata={
            "name": "EncumbranceNeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
