from __future__ import annotations

from dataclasses import dataclass

from .publication_delivery_structure import PublicationDeliveryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PublicationDelivery(PublicationDeliveryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
