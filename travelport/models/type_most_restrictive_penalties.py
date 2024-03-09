from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_restriction_data import TypeRestrictionData

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeMostRestrictivePenalties:
    """
    Most Restrictive Penalties.

    Parameters
    ----------
    restriction_type
        Contain the type of restriction applicable
    """

    class Meta:
        name = "typeMostRestrictivePenalties"

    restriction_type: list[TypeRestrictionData] = field(
        default_factory=list,
        metadata={
            "name": "RestrictionType",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
