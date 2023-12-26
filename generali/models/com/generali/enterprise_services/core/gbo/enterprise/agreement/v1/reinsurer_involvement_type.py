from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_type import (
    ValueType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.cover_type_enum import (
    CoverTypeEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type_reinsurance_nature import (
    ReinsurerInvolvementTypeReinsuranceNature,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type_reinsurance_type import (
    ReinsurerInvolvementTypeReinsuranceType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.reinsurer_involvement_type_ritaxes_apply_to import (
    ReinsurerInvolvementTypeRitaxesApplyTo,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.insurer_role_type import (
    InsurerRoleType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_involvement_type import (
    OrganisationInvolvementType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ReinsurerInvolvementType(OrganisationInvolvementType):
    organisation_role: Optional[InsurerRoleType] = field(
        default=None,
        metadata={
            "name": "OrganisationRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    policy_identifier: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "PolicyIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    sequence_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    parent_sequence_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ParentSequenceNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    risk_share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    retained_risk_share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RetainedRiskShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    overrider_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OverriderPercentage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    cover_type: Optional[CoverTypeEnum] = field(
        default=None,
        metadata={
            "name": "CoverType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    local_ceded_share: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LocalCededShare",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    ritaxes: Optional[ValueType] = field(
        default=None,
        metadata={
            "name": "RITaxes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    ritaxes_apply_to: Optional[ReinsurerInvolvementTypeRitaxesApplyTo] = field(
        default=None,
        metadata={
            "name": "RITaxesApplyTo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    reinsurance_nature: Optional[
        ReinsurerInvolvementTypeReinsuranceNature
    ] = field(
        default=None,
        metadata={
            "name": "ReinsuranceNature",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    reinsurance_type: Optional[
        ReinsurerInvolvementTypeReinsuranceType
    ] = field(
        default=None,
        metadata={
            "name": "ReinsuranceType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
