from __future__ import annotations

from dataclasses import dataclass

from .type_of_travel_document_ref_structure import (
    TypeOfTravelDocumentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTravelDocumentRef(TypeOfTravelDocumentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
