from dataclasses import dataclass, field
from typing import List

from .info_link import InfoLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfoLinksRelStructure:
    class Meta:
        name = "infoLinks_RelStructure"

    info_link: List[InfoLink] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
