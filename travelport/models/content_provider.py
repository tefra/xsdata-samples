from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.content_provider_agency_credentials import (
    ContentProviderAgencyCredentials,
)
from travelport.models.type_provider_supplier_capability_type import (
    TypeProviderSupplierCapabilityType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ContentProvider:
    """
    A content provider uniquely identified with its provider code and supplier
    code.If a given provider provides content for multiple suppliers, multiple
    elements will be returned for that provider.

    Parameters
    ----------
    provider_code
        The host for the content (e.g.1G,1P,1S,1A,ACH,MCH).
    supplier_code
        Indicates the direct connect supplier (e.g. U2) when the provider is
        a hub (e.g. ACH).
    agency_credentials
        Indicates whether agency (or agent ) credentials are required to
        connect to the given provider/supplier.
    active
        Status of the given provider/supplier . If not currently active, a
        user cannot connect to the given provider/supplier.
    provisionable
        Indicates whether the given provider/supplier can be provisioned to
        an agency/branch/agent.
    merchandising_achadapter
        ACH adapter for Merchandising ACH carrier.
    static_data_carrier
        Returns "true" if it is StaticDataCarrier otherwise "false". Default
        value is "false".
    merchandising_achcarrier
        Returns "true" if it is MerchandisingACHCarrier otherwise "false".
        Default value is "false".
    merchandising_hub_carrier
        Returns "true" if it is MerchandisingHubCarrier otherwise "false".
        Default value is "false".
    booking_retrieve
        Indication if a Provider and/or Supplier has booking retrieve
        capability.
    segment_modify
        Indication if a Provider and/or Supplier has booking segment modify
        capability.
    optional_services_modify
        Indication if a Provider and/or Supplier has booking optional
        service modify capability.
    traveler_info_modify
        Indication if a Provider and/or Supplier has traveler information
        modify capability.
    additional_payment
        Indication if a Provider and/or Supplier has additional payment
        capability.
    booking_cancel
        Indication if a Provider and/or Supplier has booking cancel
        capability.
    seat_map
        Indication if a Provider and/or Supplier has SeatMap capability.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        },
    )
    agency_credentials: None | ContentProviderAgencyCredentials = field(
        default=None,
        metadata={
            "name": "AgencyCredentials",
            "type": "Attribute",
            "required": True,
        },
    )
    active: None | bool = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
            "required": True,
        },
    )
    provisionable: None | bool = field(
        default=None,
        metadata={
            "name": "Provisionable",
            "type": "Attribute",
            "required": True,
        },
    )
    merchandising_achadapter: None | str = field(
        default=None,
        metadata={
            "name": "MerchandisingACHAdapter",
            "type": "Attribute",
        },
    )
    static_data_carrier: bool = field(
        default=False,
        metadata={
            "name": "StaticDataCarrier",
            "type": "Attribute",
        },
    )
    merchandising_achcarrier: bool = field(
        default=False,
        metadata={
            "name": "MerchandisingACHCarrier",
            "type": "Attribute",
        },
    )
    merchandising_hub_carrier: bool = field(
        default=False,
        metadata={
            "name": "MerchandisingHubCarrier",
            "type": "Attribute",
        },
    )
    booking_retrieve: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "BookingRetrieve",
            "type": "Attribute",
        },
    )
    segment_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "SegmentModify",
            "type": "Attribute",
        },
    )
    optional_services_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "OptionalServicesModify",
            "type": "Attribute",
        },
    )
    traveler_info_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "TravelerInfoModify",
            "type": "Attribute",
        },
    )
    additional_payment: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "AdditionalPayment",
            "type": "Attribute",
        },
    )
    booking_cancel: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "BookingCancel",
            "type": "Attribute",
        },
    )
    seat_map: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "SeatMap",
            "type": "Attribute",
        },
    )
