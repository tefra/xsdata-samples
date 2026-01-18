from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_endpoint_ref import TypeEndpointRef
from travelport.models.type_field_ref_2 import TypeFieldRef2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeEditableEndpoint(TypeEndpointRef):
    """
    Base type of an editable endpoint command.

    Parameters
    ----------
    fixed_field_ref
        A reference to a fixed field
    custom_field_ref
        A reference to a custom field
    """

    class Meta:
        name = "typeEditableEndpoint"

    fixed_field_ref: None | TypeFieldRef2 = field(
        default=None,
        metadata={
            "name": "FixedFieldRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    custom_field_ref: None | TypeFieldRef2 = field(
        default=None,
        metadata={
            "name": "CustomFieldRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
