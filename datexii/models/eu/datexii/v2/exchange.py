from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.catalogue_reference import CatalogueReference
from datexii.models.eu.datexii.v2.changed_flag_enum import ChangedFlagEnum
from datexii.models.eu.datexii.v2.deny_reason_enum import DenyReasonEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.filter_reference import FilterReference
from datexii.models.eu.datexii.v2.international_identifier import (
    InternationalIdentifier,
)
from datexii.models.eu.datexii.v2.request_type_enum import RequestTypeEnum
from datexii.models.eu.datexii.v2.response_enum import ResponseEnum
from datexii.models.eu.datexii.v2.subscription import Subscription
from datexii.models.eu.datexii.v2.target import Target

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Exchange:
    """
    Details associated with the management of the exchange between the
    supplier and the client.

    :ivar changed_flag: Indicates that either a filter or a catalogue
        has been changed.
    :ivar client_identification: In a data exchange process, an
        identifier of the organisation or group of organisations which
        receives information from the DATEX II supplier system.
    :ivar delivery_break: Indicates that a data delivery is stopped for
        unplanned reasons, i.e. excluding the end of the order validity
        (attribute FIL) or the case when the filter expression is not
        met (attribute OOR).
    :ivar deny_reason: Indicates the reason for the refusal of the
        requested exchange.
    :ivar historical_start_date: For "Client Pull" exchange mode
        (operating mode 3 - snapshot) it defines the date/time at which
        the snapshot was produced.
    :ivar historical_stop_date: For "Client Pull" exchange mode
        (operating mode 3 - snapshot) it defines the date/time after
        which the snapshot is no longer considered valid.
    :ivar keep_alive: Indicator that this exchange is due to "keep
        alive" functionality.
    :ivar request_type: The type of request that has been made by the
        client on the supplier.
    :ivar response: The type of the response that the supplier is
        returning to the requesting client.
    :ivar subscription_reference: Unique identifier of the client's
        subscription with the supplier.
    :ivar supplier_identification:
    :ivar target:
    :ivar subscription:
    :ivar filter_reference:
    :ivar catalogue_reference:
    :ivar exchange_extension:
    """

    changed_flag: ChangedFlagEnum | None = field(
        default=None,
        metadata={
            "name": "changedFlag",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    client_identification: str | None = field(
        default=None,
        metadata={
            "name": "clientIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    delivery_break: bool | None = field(
        default=None,
        metadata={
            "name": "deliveryBreak",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    deny_reason: DenyReasonEnum | None = field(
        default=None,
        metadata={
            "name": "denyReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    historical_start_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "historicalStartDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    historical_stop_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "historicalStopDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    keep_alive: bool | None = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    request_type: RequestTypeEnum | None = field(
        default=None,
        metadata={
            "name": "requestType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    response: ResponseEnum | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    subscription_reference: str | None = field(
        default=None,
        metadata={
            "name": "subscriptionReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    supplier_identification: InternationalIdentifier | None = field(
        default=None,
        metadata={
            "name": "supplierIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    target: Target | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    subscription: Subscription | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    filter_reference: list[FilterReference] = field(
        default_factory=list,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    catalogue_reference: list[CatalogueReference] = field(
        default_factory=list,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    exchange_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "exchangeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
