from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RequestTimestamp:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: None | XmlDateTime = field(
        default=None,
        metadata={
            "required": True,
        },
    )
