from __future__ import annotations

from dataclasses import dataclass

from .type_of_tariff_ref_structure import TypeOfTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTariffRef(TypeOfTariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
