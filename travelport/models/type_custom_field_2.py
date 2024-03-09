from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from travelport.models.alpha_numeric_restriction_2 import (
    AlphaNumericRestriction2,
)
from travelport.models.decimal_restriction_2 import DecimalRestriction2
from travelport.models.freeform_text_restriction_2 import (
    FreeformTextRestriction2,
)
from travelport.models.percentage_restriction_2 import PercentageRestriction2
from travelport.models.text_restriction_2 import TextRestriction2
from travelport.models.type_custom_field_data_format_2 import (
    TypeCustomFieldDataFormat2,
)
from travelport.models.type_masked_2 import TypeMasked2
from travelport.models.whole_number_restriction_2 import (
    WholeNumberRestriction2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeCustomField2:
    """
    Base representation of a custom field.

    Parameters
    ----------
    freeform_text_restriction
    whole_number_restriction
    decimal_restriction
    text_restriction
    alpha_numeric_restriction
    percentage_restriction
    id
        Unique identifier of the field.
    name
        Name of the field.
    description
        Description of the field.
    type_value
        Data type of the field (e.g., boolean, float, string, int).
    encrypted
        Defines whether the data associated to this field is to be encrypted
        in the database. Default is false.
    masked
        Defines whether the field value must be masked in messaging, and
        what masking pattern to apply.
    default_value
        Default value of the field.
    protected
        If true, then special authorization is required for a user to create
        or modify this field or group.
    display_order
        The order displayed by an UI
    inheritable
        Denotes that the custom field is inherited in child profiles.
        Defaults to false.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    """

    class Meta:
        name = "typeCustomField"

    freeform_text_restriction: None | FreeformTextRestriction2 = field(
        default=None,
        metadata={
            "name": "FreeformTextRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    whole_number_restriction: None | WholeNumberRestriction2 = field(
        default=None,
        metadata={
            "name": "WholeNumberRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    decimal_restriction: None | DecimalRestriction2 = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    text_restriction: None | TextRestriction2 = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    alpha_numeric_restriction: None | AlphaNumericRestriction2 = field(
        default=None,
        metadata={
            "name": "AlphaNumericRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    percentage_restriction: None | PercentageRestriction2 = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
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
    type_value: None | TypeCustomFieldDataFormat2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
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
    default_value: None | str = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
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
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
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
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        },
    )
