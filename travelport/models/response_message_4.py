from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.response_message_type_4 import ResponseMessageType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ResponseMessage4:
    """A simple textual fare note.

    Used within several other objects.

    Parameters
    ----------
    value
    code
    type_value
        Indicates the type of message (Warning, Error, Info)
    provider_code
    supplier_code
    """

    class Meta:
        name = "ResponseMessage"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: None | ResponseMessageType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
