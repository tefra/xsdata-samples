from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class SubDivisionType:
    subdivision_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "subdivisionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    subdivision_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "subdivisionCategory",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    subdivisions: Optional["SubdivisionsType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )


@dataclass
class SubdivisionsType:
    subdivision: List[SubDivisionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        }
    )
