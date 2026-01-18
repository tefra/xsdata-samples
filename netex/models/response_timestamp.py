from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseTimestamp:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: XmlDateTime | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
