from __future__ import annotations

from dataclasses import dataclass

from .travel_document_version_structure import TravelDocumentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocument(TravelDocumentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
