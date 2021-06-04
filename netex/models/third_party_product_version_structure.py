from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_product_version_structure import FareProductVersionStructure
from netex.models.general_group_of_entities import GeneralGroupOfEntities
from netex.models.general_group_of_entities_ref import GeneralGroupOfEntitiesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ThirdPartyProductVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "ThirdPartyProduct_VersionStructure"

    general_group_of_entities_ref: Optional[GeneralGroupOfEntitiesRef] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities: Optional[GeneralGroupOfEntities] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
