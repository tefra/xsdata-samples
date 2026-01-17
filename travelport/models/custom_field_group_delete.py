from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_custom_field_and_group_delete_ref_2 import (
    TypeCustomFieldAndGroupDeleteRef2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroupDelete(TypeCustomFieldAndGroupDeleteRef2):
    """
    Removes a Custom Field Group from a Template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
