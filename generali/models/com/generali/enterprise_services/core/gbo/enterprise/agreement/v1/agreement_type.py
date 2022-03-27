from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gbotype import BaseGbotype
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.local_data_type import LocalDataType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type_account_managers import AgreementTypeAccountManagers
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type_coinsurer_involvements import AgreementTypeCoinsurerInvolvements
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type_insured_involvement import AgreementTypeInsuredInvolvement
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type_payout_benefits import AgreementTypePayoutBenefits
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.agreement_type_underwriters import AgreementTypeUnderwriters
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.business_origin_enum import BusinessOriginEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.classification_code_enum import ClassificationCodeEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.contacts_involvement import ContactsInvolvement
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.intermediary_involvement_type import IntermediaryInvolvementType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.layer_type_enum import LayerTypeEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.line_of_business_type import LineOfBusinessType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class AgreementType(BaseGbotype):
    """
    :ivar expiry_date:
    :ivar inception_date:
    :ivar renewable:
    :ivar issue_date:
    :ivar layer_attachment_point:
    :ivar last_renewal_date:
    :ivar endorsed:
    :ivar endorsment_version:
    :ivar status:
    :ivar status_date:
    :ivar status_notes:
    :ivar sum_insured:
    :ivar total_layers:
    :ivar renewed_from:
    :ivar underwriting_year:
    :ivar version:
    :ivar account_managers:
    :ivar business_origin:
    :ivar classification_code:
    :ivar coinsurer_involvements:
    :ivar contacts:
    :ivar insured_involvement:
    :ivar intermediary:
    :ivar underwriters:
    :ivar layer_type:
    :ivar line_of_business:
    :ivar payout_benefits:
    :ivar local_currency: The currency code, should be an ISO 3 digit
        code
    :ivar remittance_currency: The currency code, should be an ISO 3
        digit code
    :ivar local_data: This element contains a key value implementation
        for local data tab.
    """
    expiry_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    inception_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InceptionDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    renewable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Renewable",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    layer_attachment_point: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "LayerAttachmentPoint",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    last_renewal_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastRenewalDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    endorsed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Endorsed",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    endorsment_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndorsmentVersion",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    status_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StatusDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    status_notes: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "StatusNotes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    sum_insured: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "SumInsured",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    total_layers: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalLayers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    renewed_from: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "RenewedFrom",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    underwriting_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnderwritingYear",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    account_managers: Optional[AgreementTypeAccountManagers] = field(
        default=None,
        metadata={
            "name": "AccountManagers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    business_origin: Optional[BusinessOriginEnum] = field(
        default=None,
        metadata={
            "name": "BusinessOrigin",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    classification_code: Optional[ClassificationCodeEnum] = field(
        default=None,
        metadata={
            "name": "ClassificationCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    coinsurer_involvements: Optional[AgreementTypeCoinsurerInvolvements] = field(
        default=None,
        metadata={
            "name": "CoinsurerInvolvements",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    contacts: Optional[ContactsInvolvement] = field(
        default=None,
        metadata={
            "name": "Contacts",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    insured_involvement: Optional[AgreementTypeInsuredInvolvement] = field(
        default=None,
        metadata={
            "name": "InsuredInvolvement",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    intermediary: List[IntermediaryInvolvementType] = field(
        default_factory=list,
        metadata={
            "name": "Intermediary",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    underwriters: Optional[AgreementTypeUnderwriters] = field(
        default=None,
        metadata={
            "name": "Underwriters",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    layer_type: Optional[LayerTypeEnum] = field(
        default=None,
        metadata={
            "name": "LayerType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    line_of_business: Optional[LineOfBusinessType] = field(
        default=None,
        metadata={
            "name": "LineOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    payout_benefits: Optional[AgreementTypePayoutBenefits] = field(
        default=None,
        metadata={
            "name": "PayoutBenefits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    local_currency: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LocalCurrency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    remittance_currency: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "RemittanceCurrency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    local_data: Optional[LocalDataType] = field(
        default=None,
        metadata={
            "name": "LocalData",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
