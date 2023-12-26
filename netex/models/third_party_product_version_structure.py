from dataclasses import dataclass, field
from typing import Optional, Union
from .fare_product_version_structure import FareProductVersionStructure
from .general_group_of_entities import GeneralGroupOfEntities
from .general_group_of_entities_ref import GeneralGroupOfEntitiesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ThirdPartyProductVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "ThirdPartyProduct_VersionStructure"

    general_group_of_entities_ref_or_general_group_of_entities: Optional[
        Union[GeneralGroupOfEntitiesRef, GeneralGroupOfEntities]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
