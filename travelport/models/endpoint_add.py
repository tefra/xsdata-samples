from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_editable_endpoint import TypeEditableEndpoint

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class EndpointAdd(TypeEditableEndpoint):
    """
    Add an endpoint to an action within a particular field or field group.

    Parameters
    ----------
    purpose_type_code
        Purpose Code is an additional piece of data that augments the link
        from endpoint to template field
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
