from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_2 import BaseRsp2
from travelport.models.field_1 import Field1
from travelport.models.field_group_1 import FieldGroup1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileSearchFieldRsp1(BaseRsp2):
    """
    Response showing details of the requested field or field group.

    Parameters
    ----------
    field_value
    field_group
        Defines the structure of a field group, which can be based on
        existing fields and groups (referred to by Id) and/or new fields and
        groups (referred to by FieldGroupRef or FieldRef and defined in
        FieldList or FieldGroupList).
    more_results
        Indicates whether more results are available that match the search
        parameters.
    """

    class Meta:
        name = "ProfileSearchFieldRsp"
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
    more_results: bool = field(
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )
