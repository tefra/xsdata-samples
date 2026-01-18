from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_1 import Provider1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class PermittedProviders1:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    provider: Provider1 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
