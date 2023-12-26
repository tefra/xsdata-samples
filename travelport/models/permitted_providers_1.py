from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_1 import Provider1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class PermittedProviders1:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    provider: None | Provider1 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
