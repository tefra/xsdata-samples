from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime


@dataclass
class Error:
    timestamp: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    code: str | None = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    message: str | None = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    payload: str | None = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
