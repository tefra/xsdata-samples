from __future__ import annotations

from dataclasses import dataclass

from .topic_structure import TopicStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Topic(TopicStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
