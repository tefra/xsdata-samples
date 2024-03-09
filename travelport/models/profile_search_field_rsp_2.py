from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_5 import BaseRsp5
from travelport.models.field_2 import Field2
from travelport.models.field_group_2 import FieldGroup2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchFieldRsp2(BaseRsp5):
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
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        },
    )
