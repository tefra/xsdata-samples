from dataclasses import dataclass
from .type_of_tariff_ref_structure import TypeOfTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTariffRef(TypeOfTariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
