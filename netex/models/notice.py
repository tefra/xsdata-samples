from dataclasses import dataclass
from netex.models.notice_version_structure import NoticeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Notice(NoticeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
