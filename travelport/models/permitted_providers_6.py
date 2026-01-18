from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_6 import Provider6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class PermittedProviders6:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    provider: Provider6 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
