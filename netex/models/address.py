from __future__ import annotations

from dataclasses import dataclass

from .address_version_structure import AddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Address(AddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
