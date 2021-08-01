from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.situation_record_extended_approved import SituationRecordExtendedApproved

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SituationRecordExtensionType:
    class Meta:
        name = "_SituationRecordExtensionType"

    situation_record_extended_approved: Optional[SituationRecordExtendedApproved] = field(
        default=None,
        metadata={
            "name": "situationRecordExtendedApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
