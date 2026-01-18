from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FareMessagesType:
    message: list[FareMessagesType.Message] = field(
        default_factory=list,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Message:
        """
        Attributes:
            airline_code:
            type_value:
            fail_code:
            info: Message text
        """

        airline_code: None | str = field(
            default=None,
            metadata={
                "name": "AirlineCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 8,
            },
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "length": 1,
            },
        )
        fail_code: None | int = field(
            default=None,
            metadata={
                "name": "FailCode",
                "type": "Attribute",
            },
        )
        info: None | str = field(
            default=None,
            metadata={
                "name": "Info",
                "type": "Attribute",
            },
        )
