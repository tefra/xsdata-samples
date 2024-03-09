from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeEndpointRef:
    """
    A reference to an endpoint.

    Parameters
    ----------
    id
        Reference to an Endpoint
    """

    class Meta:
        name = "typeEndpointRef"

    id: None | int = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
