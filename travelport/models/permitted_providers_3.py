from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_3 import Provider3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class PermittedProviders3:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    provider: None | Provider3 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
