from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.endpoint_ref import EndpointRef
from travelport.models.type_action_reference import TypeActionReference

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ActionRef(TypeActionReference):
    """
    Application of an action to a field.

    Refers to Actions retrieved in ProfileRetrieveAction service.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    endpoint_ref: list[EndpointRef] = field(
        default_factory=list,
        metadata={
            "name": "EndpointRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
