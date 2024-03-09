from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.optional_service_modifier import OptionalServiceModifier

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class OptionalServiceModifiers:
    """
    Rich Content and Branding for an optional service.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    optional_service_modifier: list[OptionalServiceModifier] = field(
        default_factory=list,
        metadata={
            "name": "OptionalServiceModifier",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
