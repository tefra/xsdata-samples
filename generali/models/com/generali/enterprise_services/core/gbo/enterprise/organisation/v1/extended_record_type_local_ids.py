from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypeLocalIds:
    class Meta:
        global_type = False

    local_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LocalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
