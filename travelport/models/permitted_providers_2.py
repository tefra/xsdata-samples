from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_2 import Provider2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class PermittedProviders2:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    provider: Provider2 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
