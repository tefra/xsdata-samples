from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeCustomFieldOrGroupType(Enum):
    """
    This is an optional field.

    If the element is not passed then the TemplateFieldID value passed will
    be considered a Fixed Field or a Fixed Field Group..
    """

    CUSTOM_FIELD = "CustomField"
    CUSTOM_FIELD_GROUP = "CustomFieldGroup"
