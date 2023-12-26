from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_action_1 import TypeAction1
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


@dataclass
class ModifyField1:
    """Details of a root-level field to be updated.

    Root-level fields cannot be created or deleted with this service.
    Child fields must be modified within ModifyFieldGroup. When updating
    a field, to remove data from an optional attribute, omit the
    attribute. Note that Display Order is not applicable to root-level
    fields.

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
    id
        Unique identifier of the field.Id is required for update or delete
        action.
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
    action
        Indicate the action to be executed (add, delete, etc.)
    force
        To specify whether this is a Force Update or Force Delete.
    """

    class Meta:
        name = "ModifyField"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    freeform_text_restriction: None | ModifyField1.FreeformTextRestriction = (
        field(
            default=None,
            metadata={
                "name": "FreeformTextRestriction",
                "type": "Element",
            },
        )
    )
    whole_number_restriction: None | ModifyField1.WholeNumberRestriction = (
        field(
            default=None,
            metadata={
                "name": "WholeNumberRestriction",
                "type": "Element",
            },
        )
    )
    decimal_restriction: None | ModifyField1.DecimalRestriction = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
        },
    )
    text_restriction: None | ModifyField1.TextRestriction = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
        },
    )
    alpha_numeric_restriction: None | ModifyField1.AlphaNumericRestriction = (
        field(
            default=None,
            metadata={
                "name": "AlphaNumericRestriction",
                "type": "Element",
            },
        )
    )
    percentage_restriction: None | ModifyField1.PercentageRestriction = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
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
    type_value: None | TypeCustomFieldDataFormat1 = field(
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
    action: None | TypeAction1 = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        },
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        },
    )

    @dataclass
    class FreeformTextRestriction(TypeStringRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class WholeNumberRestriction(TypeIntegerRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DecimalRestriction(TypeFloatRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TextRestriction(TypeStringRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (add, update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class AlphaNumericRestriction(TypeStringRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (add, update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PercentageRestriction(TypeFloatRestriction1):
        """
        Parameters
        ----------
        action
            Indicate the action to be executed (add, update or delete)
        """

        action: None | TypeAction1 = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            },
        )
