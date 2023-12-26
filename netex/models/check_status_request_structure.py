from dataclasses import dataclass, field
from typing import Optional
from .extensions_1 import Extensions1
from .request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusRequestStructure(RequestStructure):
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )
