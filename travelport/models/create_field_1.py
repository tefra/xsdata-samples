from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_custom_field_data_format_1 import (
    TypeCustomFieldDataFormat1,
)
from travelport.models.type_float_restriction_1 import TypeFloatRestriction1
from travelport.models.type_integer_restriction_1 import (
    TypeIntegerRestriction1,
)
from travelport.models.type_masked_1 import TypeMasked1
from travelport.models.type_string_restriction_1 import TypeStringRestriction1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class CreateField1:
    """
    Specify any existing fields that belong to this group.

    Parameters
    ----------
    freeform_text_restriction
        Restrictions on profile data for fields with a data type of free-
        form text (i.e., string). Min and max lengths are inclusive. Can
        define either min/max lengths or enumerations, but not both.
    whole_number_restriction
        Restrictions on profile data for fields with a data type of integer.
        Min and max values are inclusive.
    decimal_restriction
        Restrictions on profile data for fields with a data type of float.
        Min and max values are inclusive.
    text_restriction
        Restrictions on profile data for fields with a data type of text
        (i.e., alpha). Min and max lengths are inclusive. Can define either
        min/max lengths or enumerations, but not both.
    alpha_numeric_restriction
        Restrictions on profile data for fields with a data type of
        alphanumeric. Min and max lengths are inclusive. Can define either
        min/max lengths or enumerations, but not both.
    percentage_restriction
        Restrictions on profile data for fields with a data type of
        percentage. Min and max values are inclusive.
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
        name = "CreateField"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    freeform_text_restriction: None | TypeStringRestriction1 = field(
        default=None,
        metadata={
            "name": "FreeformTextRestriction",
            "type": "Element",
        },
    )
    whole_number_restriction: None | TypeIntegerRestriction1 = field(
        default=None,
        metadata={
            "name": "WholeNumberRestriction",
            "type": "Element",
        },
    )
    decimal_restriction: None | TypeFloatRestriction1 = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
        },
    )
    text_restriction: None | TypeStringRestriction1 = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
        },
    )
    alpha_numeric_restriction: None | TypeStringRestriction1 = field(
        default=None,
        metadata={
            "name": "AlphaNumericRestriction",
            "type": "Element",
        },
    )
    percentage_restriction: None | TypeFloatRestriction1 = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
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
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    type_value: TypeCustomFieldDataFormat1 = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        },
    )
    masked: TypeMasked1 = field(
        default=TypeMasked1.NOT_MASKED,
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
