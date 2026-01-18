from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_editable_custom_field_2 import (
    TypeEditableCustomField2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class CustomFieldAdd(TypeEditableCustomField2):
    """
    Add Custom field to the template.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
