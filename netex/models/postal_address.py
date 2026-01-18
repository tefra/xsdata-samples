from __future__ import annotations

from dataclasses import dataclass

from .postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PostalAddress(PostalAddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
