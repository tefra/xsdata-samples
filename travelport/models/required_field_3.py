from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_name_3 import RequiredFieldName3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class RequiredField3:
    """
    Parameters
    ----------
    name
        The name of the required field
    """

    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    name: None | RequiredFieldName3 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
