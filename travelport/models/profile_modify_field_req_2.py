from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.modify_field_2 import ModifyField2
from travelport.models.modify_field_group_2 import ModifyFieldGroup2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyFieldReq2(BaseReq5):
    """Modifies a custom field or field group.

    Note that some modifications are not permitted once a field or field
    group is in use (i.e., is associated to a template).
    """
    class Meta:
        name = "ProfileModifyFieldReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    modify_field: list[ModifyField2] = field(
        default_factory=list,
        metadata={
            "name": "ModifyField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    modify_field_group: list[ModifyFieldGroup2] = field(
        default_factory=list,
        metadata={
            "name": "ModifyFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )
