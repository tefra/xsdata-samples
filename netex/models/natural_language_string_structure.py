from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguageStringStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
