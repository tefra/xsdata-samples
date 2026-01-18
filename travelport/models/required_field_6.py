from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.required_field_name_6 import RequiredFieldName6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class RequiredField6:
    """
    Parameters
    ----------
    name
        The name of the required field
    """

    class Meta:
        name = "RequiredField"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    name: RequiredFieldName6 = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
