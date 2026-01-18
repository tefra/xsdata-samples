from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_2 import BaseReq2
from travelport.models.modify_field_1 import ModifyField1
from travelport.models.modify_field_group_1 import ModifyFieldGroup1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileModifyFieldReq1(BaseReq2):
    """
    Modifies a custom field or field group.

    Note that some modifications are not permitted once a field or field
    group is in use (i.e., is associated to a template).
    """

    class Meta:
        name = "ProfileModifyFieldReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    modify_field: list[ModifyField1] = field(
        default_factory=list,
        metadata={
            "name": "ModifyField",
            "type": "Element",
        },
    )
    modify_field_group: list[ModifyFieldGroup1] = field(
        default_factory=list,
        metadata={
            "name": "ModifyFieldGroup",
            "type": "Element",
        },
    )
