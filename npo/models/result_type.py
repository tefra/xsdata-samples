from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.total_qualifier import TotalQualifier

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ResultType:
    class Meta:
        name = "resultType"

    items: Optional["ResultType.Items"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    total: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    total_qualifier: Optional[TotalQualifier] = field(
        default=None,
        metadata={
            "name": "totalQualifier",
            "type": "Attribute",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Items:
        item: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )
