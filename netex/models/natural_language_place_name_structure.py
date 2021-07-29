from dataclasses import dataclass, field
from typing import Optional
from .lang_value import LangValue

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguagePlaceNameStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[^,\[\]\{\}\?$%\^=@#;:]+",
        }
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
