from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_5 import Provider5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class PermittedProviders5:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    provider: None | Provider5 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
