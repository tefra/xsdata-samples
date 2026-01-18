from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataNameSpacesStructure:
    stop_point_name_space: None | str = field(
        default=None,
        metadata={
            "name": "StopPointNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_name_space: None | str = field(
        default=None,
        metadata={
            "name": "LineNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_name_space: None | str = field(
        default=None,
        metadata={
            "name": "ProductCategoryNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_name_space: None | str = field(
        default=None,
        metadata={
            "name": "ServiceFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_name_space: None | str = field(
        default=None,
        metadata={
            "name": "VehicleFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
