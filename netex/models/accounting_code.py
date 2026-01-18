from __future__ import annotations

from dataclasses import dataclass

from .private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccountingCode(PrivateCodeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
