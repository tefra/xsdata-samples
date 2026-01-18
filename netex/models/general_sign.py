from __future__ import annotations

from dataclasses import dataclass

from .general_sign_structure import GeneralSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralSign(GeneralSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
