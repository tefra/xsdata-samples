from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class SubdivisionsType:
    subdivision: list[SubDivisionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SubDivisionType:
    subdivision_code: None | str = field(
        default=None,
        metadata={
            "name": "subdivisionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    subdivision_category: None | str = field(
        default=None,
        metadata={
            "name": "subdivisionCategory",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    subdivisions: None | SubdivisionsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
