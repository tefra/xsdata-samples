from __future__ import annotations

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


@dataclass(kw_only=True)
class ClaimType:
    claim_number: str = field(
        metadata={
            "name": "ClaimNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    policy_number: str = field(
        metadata={
            "name": "PolicyNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    source: str = field(
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    contact: str = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    interest: None | str = field(
        default=None,
        metadata={
            "name": "Interest",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_open: DateTimeType = field(
        metadata={
            "name": "DateOpen",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    date_last_transaction: DateTimeType = field(
        metadata={
            "name": "DateLastTransaction",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    date_of_loss: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "DateOfLoss",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_reported: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "DateReported",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    date_last_updated: DateTimeType = field(
        metadata={
            "name": "DateLastUpdated",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    last_update_by: str = field(
        metadata={
            "name": "LastUpdateBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    adjuster: None | str = field(
        default=None,
        metadata={
            "name": "Adjuster",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    comments: None | str = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    cause_of_loss: None | str = field(
        default=None,
        metadata={
            "name": "CauseOfLoss",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    loss_description: None | str = field(
        default=None,
        metadata={
            "name": "LossDescription",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    location_key: None | str = field(
        default=None,
        metadata={
            "name": "LocationKey",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    address: None | AddressType = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    currency: str = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    deductibles: AmountType = field(
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    paid_claim: AmountType = field(
        metadata={
            "name": "PaidClaim",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    paid_vendor_fee: AmountType = field(
        metadata={
            "name": "PaidVendorFee",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    recovery_reserve: None | AmountType = field(
        default=None,
        metadata={
            "name": "RecoveryReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    claim_reserve: AmountType = field(
        metadata={
            "name": "ClaimReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    vendor_fee_reserve: AmountType = field(
        metadata={
            "name": "VendorFeeReserve",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    total_incurred: None | AmountType = field(
        default=None,
        metadata={
            "name": "TotalIncurred",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    producing_office_contact: None | str = field(
        default=None,
        metadata={
            "name": "ProducingOfficeContact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    fronting_office_contact: None | str = field(
        default=None,
        metadata={
            "name": "FrontingOfficeContact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
