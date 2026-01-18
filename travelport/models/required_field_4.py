from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.required_field_name_4 import RequiredFieldName4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class RequiredField4:
    """
    Parameters
    ----------
    name
        The name of the required field
    """

    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    name: RequiredFieldName4 = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
