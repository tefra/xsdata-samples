from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.field_2 import Field2
from travelport.models.field_group_2 import FieldGroup2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyFieldRsp2(BaseRsp5):
    """
    Response reflecting changes made to the custom field or field group.

    Parameters
    ----------
    field_value
        Defines a field.
    field_group
        Defines a field group.
    """

    class Meta:
        name = "ProfileModifyFieldRsp"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_value: list[Field2] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    field_group: list[FieldGroup2] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
            "max_occurs": 999,
        },
    )
