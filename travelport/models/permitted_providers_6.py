from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_6 import Provider6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class PermittedProviders6:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    provider: None | Provider6 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
