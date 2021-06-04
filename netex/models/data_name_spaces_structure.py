from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataNameSpacesStructure:
    stop_point_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    line_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    product_category_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    service_feature_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    vehicle_feature_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
