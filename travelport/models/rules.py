from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Rules:
    """
    Parameters
    ----------
    rules_text
        Rules text
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    rules_text: None | str = field(
        default=None,
        metadata={
            "name": "RulesText",
            "type": "Element",
        },
    )
