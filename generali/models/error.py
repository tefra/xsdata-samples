from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class Error:
    timestamp: XmlDateTime = field(
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    code: str = field(
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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
