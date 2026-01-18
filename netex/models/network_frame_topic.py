from __future__ import annotations

from dataclasses import dataclass

from .network_frame_topic_structure import NetworkFrameTopicStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkFrameTopic(NetworkFrameTopicStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
