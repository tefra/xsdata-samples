from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.action_ref import ActionRef
from travelport.models.fixed_field_group_ref import FixedFieldGroupRef
from travelport.models.type_fixed_field_data_format import (
    TypeFixedFieldDataFormat,
)
from travelport.models.type_masked_2 import TypeMasked2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class FixedField:
    """
    Specify existing fixed fields that belong to the default template.

    Parameters
    ----------
    fixed_field_group_ref
    action_ref
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
    name
        Name of the field.
    data_type
        Data type of the field (e.g., boolean, float, string, int).
    component
        The corresponding name of the attribute or sub-element that this
        field refers to in the profile message.  This is a read only field.
    description
        Description of the Fixed Field as defined by the system.
    encrypted
        Defines whether the data associated to this field is to be encrypted
        in the database. Default is false.
    masked
        Defines whether the field value must be masked in messaging, and
        what masking pattern to apply.
    searchable
        Flag to indicate if the field is searchable.
    inheritable
        A flag to indicate if the field can be inherited. Default to false.
        Only applies to root level fields. Fields within field groups are
        not inheritable.
    read_only
        Defines if field as editable or not.
    overriden
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field_group_ref: list[FixedFieldGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroupRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    action_ref: list[ActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    id: str = field(
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
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        },
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        },
    )
    search_option_display_order: None | int = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        },
    )
    min_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        },
    )
    max_occurs_override: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        },
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        },
    )
    min_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    data_type: TypeFixedFieldDataFormat = field(
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        }
    )
    component: None | str = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        },
    )
    masked: TypeMasked2 = field(
        default=TypeMasked2.NOT_MASKED,
        metadata={
            "name": "Masked",
            "type": "Attribute",
        },
    )
    searchable: bool = field(
        metadata={
            "name": "Searchable",
            "type": "Attribute",
            "required": True,
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        },
    )
    read_only: None | bool = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        },
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        },
    )
