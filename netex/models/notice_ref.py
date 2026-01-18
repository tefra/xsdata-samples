from __future__ import annotations

from dataclasses import dataclass

from .notice_ref_structure import NoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeRef(NoticeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
