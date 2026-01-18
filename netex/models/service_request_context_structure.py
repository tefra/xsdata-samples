from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .data_name_spaces_structure import DataNameSpacesStructure
from .delivery_method_enumeration import DeliveryMethodEnumeration
from .empty_type_1 import EmptyType1
from .predictors_enumeration import PredictorsEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequestContextStructure:
    check_status_address: str | None = field(
        default=None,
        metadata={
            "name": "CheckStatusAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscribe_address: str | None = field(
        default=None,
        metadata={
            "name": "SubscribeAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manage_subscription_address: str | None = field(
        default=None,
        metadata={
            "name": "ManageSubscriptionAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    get_data_address: str | None = field(
        default=None,
        metadata={
            "name": "GetDataAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status_response_address: str | None = field(
        default=None,
        metadata={
            "name": "StatusResponseAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_address: str | None = field(
        default=None,
        metadata={
            "name": "SubscriberAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_address: str | None = field(
        default=None,
        metadata={
            "name": "NotifyAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consumer_address: str | None = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_name_spaces: DataNameSpacesStructure | None = field(
        default=None,
        metadata={
            "name": "DataNameSpaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: str | None = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    wgs_decimal_degrees_or_gml_coordinate_format: EmptyType1 | str | None = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "WgsDecimalDegrees",
                        "type": EmptyType1,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "GmlCoordinateFormat",
                        "type": str,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
    )
    distance_units: str | None = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity_units: str | None = field(
        default=None,
        metadata={
            "name": "VelocityUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_horizon: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "DataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timeout: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "RequestTimeout",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delivery_method: DeliveryMethodEnumeration | None = field(
        default=None,
        metadata={
            "name": "DeliveryMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    multipart_despatch: bool | None = field(
        default=None,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confirm_delivery: bool | None = field(
        default=None,
        metadata={
            "name": "ConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximimum_number_of_subscriptions: int | None = field(
        default=None,
        metadata={
            "name": "MaximimumNumberOfSubscriptions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_predictors: PredictorsEnumeration | None = field(
        default=None,
        metadata={
            "name": "AllowedPredictors",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_function: str | None = field(
        default=None,
        metadata={
            "name": "PredictionFunction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
