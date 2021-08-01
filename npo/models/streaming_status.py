from dataclasses import dataclass, field
from typing import Optional
from npo.models.streaming_status_value import StreamingStatusValue

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class StreamingStatus:
    class Meta:
        name = "streamingStatus"
        namespace = "urn:vpro:media:2009"

    with_drm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "name": "withDrm",
            "type": "Attribute",
        }
    )
    without_drm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "name": "withoutDrm",
            "type": "Attribute",
        }
    )
