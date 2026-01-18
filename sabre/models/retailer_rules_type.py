from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class RetailerRulesType:
    """
    Attributes:
        retailer_rule:
        force: If set to true, only fares with a matched Business Rule
            containing the specified Retailer Rule Qualifier will be
            returned
    """

    retailer_rule: list[RetailerRulesType.RetailerRule] = field(
        default_factory=list,
        metadata={
            "name": "RetailerRule",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class RetailerRule:
        code: str = field(
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9a-zA-Z]{2,20}",
            }
        )
