from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass
class Error:
    timestamp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
    payload: None | str = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        },
    )
