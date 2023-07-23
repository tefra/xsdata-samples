from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FixedFieldUpdate:
    """Update the agency-defined attributes for a fixed field.

    To remove a value, omit the attribute entirely.

    Parameters
    ----------
    id
        Unique identifier of the field.
    label
        Alternate name of the field for display on the UI
    display_order
        The order displayed by an UI
    hide
        A flag the determines if the UI should show this field.  Default to
        false.
    search_option
        If true, then this field is identified as one that is allowed to be
        searched on.  It is user defined.
    search_option_display_order
        The display order for search option.
    min_occurs_override
        Minimum Agency-defined override defining the minimum number of
        instances permitted by the agency.
    max_occurs_override
        Maximum Agency-defined override defining the maximum number of
        instances permitted by the agency.
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).  Leave blank to
        indicate 0.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        }
    )
    search_option_display_order: None | int = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        }
    )
    min_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    min_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
