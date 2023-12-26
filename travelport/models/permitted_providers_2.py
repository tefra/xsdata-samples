from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_2 import Provider2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class PermittedProviders2:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    provider: None | Provider2 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
