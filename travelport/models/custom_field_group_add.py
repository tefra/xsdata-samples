from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_common_editable_group_2 import (
    TypeCommonEditableGroup2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class CustomFieldGroupAdd(TypeCommonEditableGroup2):
    """
    Add custom field group to the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
