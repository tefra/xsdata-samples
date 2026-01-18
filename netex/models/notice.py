from __future__ import annotations

from dataclasses import dataclass

from .notice_version_structure import NoticeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Notice(NoticeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
