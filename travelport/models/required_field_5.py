from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.required_field_name_5 import RequiredFieldName5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class RequiredField5:
    """
    Parameters
    ----------
    name
        The name of the required field
    """
    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    name: None | RequiredFieldName5 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
