from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractItemStructure:
    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
