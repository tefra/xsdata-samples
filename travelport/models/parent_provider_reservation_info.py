from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.pnrdivide_info import PnrdivideInfo

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ParentProviderReservationInfo(PnrdivideInfo):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
