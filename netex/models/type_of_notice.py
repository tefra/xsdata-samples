from __future__ import annotations

from dataclasses import dataclass

from .type_of_notice_value_structure import TypeOfNoticeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfNotice(TypeOfNoticeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
