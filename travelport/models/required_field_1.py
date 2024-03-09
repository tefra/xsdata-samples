from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.required_field_name_1 import RequiredFieldName1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class RequiredField1:
    """
    Parameters
    ----------
    name
        The name of the required field
    """

    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    name: None | RequiredFieldName1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
