from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_common_editable_group_2 import (
    TypeCommonEditableGroup2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroupUpdate(TypeCommonEditableGroup2):
    """
    Modify the agency-defined attributes of a custom field group already associated
    with the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
