from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.response_message_type_6 import ResponseMessageType6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class ResponseMessage6:
    """
    A simple textual fare note.

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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: int = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | ResponseMessageType6 = field(
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
