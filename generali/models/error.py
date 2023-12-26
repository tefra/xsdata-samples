from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class Error:
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    payload: Optional[str] = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
