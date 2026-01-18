from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.streaming_status_value import StreamingStatusValue

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class StreamingStatus:
    class Meta:
        name = "streamingStatus"
        namespace = "urn:vpro:media:2009"

    with_drm: None | StreamingStatusValue = field(
        default=None,
        metadata={
            "name": "withDrm",
            "type": "Attribute",
        },
    )
    without_drm: None | StreamingStatusValue = field(
        default=None,
        metadata={
            "name": "withoutDrm",
            "type": "Attribute",
        },
    )
