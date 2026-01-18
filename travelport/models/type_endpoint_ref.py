from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
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

    id: int = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
