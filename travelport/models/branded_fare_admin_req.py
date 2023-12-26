from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.fare_family_add import FareFamilyAdd
from travelport.models.fare_family_delete import FareFamilyDelete
from travelport.models.fare_family_update import FareFamilyUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class BrandedFareAdminReq(BaseReq1):
    """
    Admin request to add/update or delete Branded fare.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_add: list[FareFamilyAdd] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyAdd",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_family_update: list[FareFamilyUpdate] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyUpdate",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_family_delete: list[FareFamilyDelete] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyDelete",
            "type": "Element",
            "max_occurs": 999,
        },
    )
