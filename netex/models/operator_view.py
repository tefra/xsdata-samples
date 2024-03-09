from dataclasses import dataclass

from .operator_derived_view_structure import OperatorDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatorView(OperatorDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
