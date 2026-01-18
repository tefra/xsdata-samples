from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MultilingualString:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text_id_type: str | None = field(
        default=None,
        metadata={
            "name": "textIdType",
            "type": "Attribute",
        },
    )
