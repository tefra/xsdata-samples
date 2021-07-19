from dataclasses import dataclass, field
from typing import Optional
from .lang_value import LangValue

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguageStringStructure:
    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
        }
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
