from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .data_name_spaces_structure import DataNameSpacesStructure
from .delivery_method_enumeration import DeliveryMethodEnumeration
from .empty_type_1 import EmptyType1
from .predictors_enumeration import PredictorsEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequestContextStructure:
    check_status_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckStatusAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscribe_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscribeAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    manage_subscription_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManageSubscriptionAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    get_data_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "GetDataAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    status_response_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusResponseAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscriber_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    notify_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotifyAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_name_spaces: Optional[DataNameSpacesStructure] = field(
        default=None,
        metadata={
            "name": "DataNameSpaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    wgs_decimal_degrees: Optional[EmptyType1] = field(
        default=None,
        metadata={
            "name": "WgsDecimalDegrees",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    gml_coordinate_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "GmlCoordinateFormat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    distance_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    velocity_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "VelocityUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_horizon: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    request_timeout: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RequestTimeout",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delivery_method: Optional[DeliveryMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "DeliveryMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    multipart_despatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    confirm_delivery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    maximimum_number_of_subscriptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximimumNumberOfSubscriptions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    allowed_predictors: Optional[PredictorsEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedPredictors",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    prediction_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "PredictionFunction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
