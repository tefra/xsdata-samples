from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.catalogue_reference import CatalogueReference
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.filter_reference import FilterReference
from datexii.models.eu.datexii.v2.operating_mode_enum import OperatingModeEnum
from datexii.models.eu.datexii.v2.subscription_state_enum import (
    SubscriptionStateEnum,
)
from datexii.models.eu.datexii.v2.target import Target
from datexii.models.eu.datexii.v2.update_method_enum import UpdateMethodEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Subscription:
    """
    This item contains all information relating to a customer subscription.

    :ivar delete_subscription: Indicates that this subscription has to
        be deleted.
    :ivar delivery_interval: Value of the interval of data delivery in
        the "periodic" delivery mode.
    :ivar operating_mode: The mode of operation of the exchange.
    :ivar subscription_start_time: Gives the date/time at which the
        subscription becomes active.
    :ivar subscription_state: The current state of the the client's
        subscription.
    :ivar subscription_stop_time: Gives the date/time at which the
        subscription expires.
    :ivar update_method: The type of updates of situations requested by
        the client.
    :ivar target:
    :ivar filter_reference:
    :ivar catalogue_reference:
    :ivar subscription_extension:
    """

    delete_subscription: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteSubscription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    delivery_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "deliveryInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    operating_mode: Optional[OperatingModeEnum] = field(
        default=None,
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    subscription_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    subscription_state: Optional[SubscriptionStateEnum] = field(
        default=None,
        metadata={
            "name": "subscriptionState",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    subscription_stop_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStopTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    update_method: Optional[UpdateMethodEnum] = field(
        default=None,
        metadata={
            "name": "updateMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    target: list[Target] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    filter_reference: Optional[FilterReference] = field(
        default=None,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    catalogue_reference: Optional[CatalogueReference] = field(
        default=None,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    subscription_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subscriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
