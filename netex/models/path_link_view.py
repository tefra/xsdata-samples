from dataclasses import dataclass, field
from typing import Any

from .path_link_derived_view_structure import PathLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkView(PathLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
