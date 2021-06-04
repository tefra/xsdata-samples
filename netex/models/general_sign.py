from dataclasses import dataclass
from netex.models.general_sign_structure import GeneralSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralSign(GeneralSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
