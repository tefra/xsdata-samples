from __future__ import annotations

from dataclasses import dataclass

from .heading_sign_ref_structure import HeadingSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HeadingSignRef(HeadingSignRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
