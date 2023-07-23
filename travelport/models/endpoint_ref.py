from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_endpoint_ref import TypeEndpointRef

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class EndpointRef(TypeEndpointRef):
    """
    A reference to an endpoint.

    Parameters
    ----------
    purpose_type_code
        Purpose Code is an additional piece of data that augments the link
        from endpoint to template field
    end_point_code
        End Point Code description.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    purpose_type_code: None | str = field(
        default=None,
        metadata={
            "name": "PurposeTypeCode",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    end_point_code: None | str = field(
        default=None,
        metadata={
            "name": "EndPointCode",
            "type": "Attribute",
            "required": True,
        }
    )
