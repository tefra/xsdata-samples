from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.field_1 import Field1
from travelport.models.field_group_1 import FieldGroup1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileModifyFieldRsp1(BaseRsp2):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    field_value: list[Field1] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        },
    )
    field_group: list[FieldGroup1] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
        },
    )
