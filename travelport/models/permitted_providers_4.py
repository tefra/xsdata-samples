from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_4 import Provider4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class PermittedProviders4:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    provider: None | Provider4 = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        },
    )
