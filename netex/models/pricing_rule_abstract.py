from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PricingRuleAbstract(DataManagedObjectStructure):
    class Meta:
        name = "PricingRule_"
        namespace = "http://www.netex.org.uk/netex"
