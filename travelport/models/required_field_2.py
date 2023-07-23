from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_name_2 import RequiredFieldName2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class RequiredField2:
    """
    Parameters
    ----------
    name
        The name of the required field
    """
    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    name: None | RequiredFieldName2 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
