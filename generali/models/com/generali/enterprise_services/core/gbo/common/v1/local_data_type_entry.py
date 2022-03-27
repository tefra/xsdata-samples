from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class LocalDataTypeEntry:
    class Meta:
        global_type = False

    value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
