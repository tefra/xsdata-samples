from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_5 import Provider5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class PermittedProviders5:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    provider: Provider5 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
