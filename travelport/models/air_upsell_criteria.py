from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_upsell_add import AirUpsellAdd
from travelport.models.air_upsell_delete import AirUpsellDelete
from travelport.models.air_upsell_update import AirUpsellUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AirUpsellCriteria:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_add: list[AirUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_upsell_update: list[AirUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_upsell_delete: list[AirUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        }
    )
