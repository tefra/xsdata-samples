from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class RecordIdentifier:
    """
    The information that uniquly identifies a particular supplier
    reservation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_locator_code: str = field(
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        },
    )
