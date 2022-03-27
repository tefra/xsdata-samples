from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypeSenders:
    class Meta:
        global_type = False

    sender: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
