from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.total_qualifier import TotalQualifier

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ResultType:
    class Meta:
        name = "resultType"

    items: None | ResultType.Items = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    total: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    total_qualifier: None | TotalQualifier = field(
        default=None,
        metadata={
            "name": "totalQualifier",
            "type": "Attribute",
        }
    )
    offset: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Items:
        item: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )
