from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class NotificationUrltype:
    """
    NotificationURLType describes the structure of an http or email
    address.

    The content holds the addresses while an attribute indicates whether or
    not is expects the contents in a SOAP message.

    :ivar value:
    :ivar is_soap: The isSOAP attribute, if true, indicates the provided
        URL expects the notification to be sent in a SOAP message.
    """

    class Meta:
        name = "NotificationURLType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    is_soap: bool = field(
        default=False,
        metadata={
            "name": "isSOAP",
            "type": "Attribute",
        },
    )
