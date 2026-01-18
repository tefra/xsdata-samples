from __future__ import annotations

from dataclasses import dataclass

from .pocd_mt000040 import PocdMt000040ClinicalDocument

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class ClinicalDocument(PocdMt000040ClinicalDocument):
    class Meta:
        namespace = "urn:hl7-org:v3"
