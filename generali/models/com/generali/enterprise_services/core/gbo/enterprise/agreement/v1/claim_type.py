from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import (
    AddressType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ClaimType:
    claim_number: str | None = field(
        default=None,
        metadata={
            "name": "ClaimNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    policy_number: str | None = field(
        default=None,
        metadata={
            "name": "PolicyNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    status: str | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    source: str | None = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    contact: str | None = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    interest: str | None = field(
        default=None,
        metadata={
            "name": "Interest",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_open: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "DateOpen",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    date_last_transaction: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "DateLastTransaction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    date_of_loss: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "DateOfLoss",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_reported: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "DateReported",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_last_updated: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "DateLastUpdated",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    last_update_by: str | None = field(
        default=None,
        metadata={
            "name": "LastUpdateBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    adjuster: str | None = field(
        default=None,
        metadata={
            "name": "Adjuster",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    comments: str | None = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    cause_of_loss: str | None = field(
        default=None,
        metadata={
            "name": "CauseOfLoss",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    loss_description: str | None = field(
        default=None,
        metadata={
            "name": "LossDescription",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    location_key: str | None = field(
        default=None,
        metadata={
            "name": "LocationKey",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    address: AddressType | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    currency: str | None = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    deductibles: AmountType | None = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    paid_claim: AmountType | None = field(
        default=None,
        metadata={
            "name": "PaidClaim",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    paid_vendor_fee: AmountType | None = field(
        default=None,
        metadata={
            "name": "PaidVendorFee",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    recovery_reserve: AmountType | None = field(
        default=None,
        metadata={
            "name": "RecoveryReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    claim_reserve: AmountType | None = field(
        default=None,
        metadata={
            "name": "ClaimReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    vendor_fee_reserve: AmountType | None = field(
        default=None,
        metadata={
            "name": "VendorFeeReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    total_incurred: AmountType | None = field(
        default=None,
        metadata={
            "name": "TotalIncurred",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    producing_office_contact: str | None = field(
        default=None,
        metadata={
            "name": "ProducingOfficeContact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    fronting_office_contact: str | None = field(
        default=None,
        metadata={
            "name": "FrontingOfficeContact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
