from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_3 import Provider3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class PermittedProviders3:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    provider: Provider3 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
