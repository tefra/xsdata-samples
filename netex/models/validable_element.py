from __future__ import annotations

from dataclasses import dataclass

from .validable_element_version_structure import (
    ValidableElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElement(ValidableElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
