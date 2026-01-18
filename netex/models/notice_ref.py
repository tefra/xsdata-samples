from __future__ import annotations

from dataclasses import dataclass

from .notice_ref_structure import NoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeRef(NoticeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
