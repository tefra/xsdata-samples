from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_custom_field_or_group_type import (
    TypeCustomFieldOrGroupType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class DeleteOverrideDefinition:
    """
    Delete existing override Definition.

    Parameters
    ----------
    template_field_id
        Unique identifier of the base template field or group id .
    template_field_type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_field_id: str = field(
        metadata={
            "name": "TemplateFieldID",
            "type": "Attribute",
            "required": True,
        }
    )
    template_field_type: None | TypeCustomFieldOrGroupType = field(
        default=None,
        metadata={
            "name": "TemplateFieldType",
            "type": "Attribute",
        },
    )
