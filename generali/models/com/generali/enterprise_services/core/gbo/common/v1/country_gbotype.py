from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.subdivisions_type import (
    SubdivisionsType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CountryGbotype:
    class Meta:
        name = "CountryGBOType"

    isocode2: str | None = field(
        default=None,
        metadata={
            "name": "ISOCode2",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
            "pattern": r"[A-Z][A-Z]",
        },
    )
    isocode3: str | None = field(
        default=None,
        metadata={
            "name": "ISOCode3",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    name: TextType | None = field(
        default=None,
        metadata={
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
