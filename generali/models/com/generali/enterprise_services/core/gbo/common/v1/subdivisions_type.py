from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class SubdivisionsType:
    subdivision: list[SubDivisionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )


@dataclass
class SubDivisionType:
    subdivision_code: str | None = field(
        default=None,
        metadata={
            "name": "subdivisionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    subdivision_category: str | None = field(
        default=None,
        metadata={
            "name": "subdivisionCategory",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    subdivisions: SubdivisionsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
