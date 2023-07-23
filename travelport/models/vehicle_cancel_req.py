from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.file_finishing_info_1 import FileFinishingInfo1
from travelport.models.vehicle import Vehicle
from travelport.models.vehicle_date_location import VehicleDateLocation

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class VehicleCancelReq(BaseReq1):
    """PNR Cancel request for a vehicle booking.

    Given a provider code and a provider locator code. This will cancel
    one or more vehicle segments based on the criteria given.  If more
    than one segment matches, then all matching will be removed.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    vehicle_date_location: None | VehicleDateLocation = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle: None | Vehicle = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    file_finishing_info: None | FileFinishingInfo1 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    supplier_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
