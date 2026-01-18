from __future__ import annotations

from dataclasses import dataclass

from .controllable_element_version_structure import (
    ControllableElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElement(ControllableElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
