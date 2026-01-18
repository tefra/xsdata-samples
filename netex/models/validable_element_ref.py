from __future__ import annotations

from dataclasses import dataclass

from .validable_element_ref_structure import ValidableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementRef(ValidableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
