from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.provider_4 import Provider4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class PermittedProviders4:
    class Meta:
        name = "PermittedProviders"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    provider: Provider4 = field(
        metadata={
            "name": "Provider",
            "type": "Element",
            "required": True,
        }
    )
