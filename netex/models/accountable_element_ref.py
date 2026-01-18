from __future__ import annotations

from dataclasses import dataclass

from .accountable_element_ref_structure import AccountableElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountableElementRef(AccountableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
