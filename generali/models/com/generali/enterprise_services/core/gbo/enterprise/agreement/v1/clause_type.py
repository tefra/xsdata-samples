from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.deductibles_type import DeductiblesType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limits_type import LimitsType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class ClauseType(BaseIdentifiedComponentType):
    code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    wording: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Wording",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    limits: Optional[LimitsType] = field(
        default=None,
        metadata={
            "name": "Limits",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    deductibles: Optional[DeductiblesType] = field(
        default=None,
        metadata={
            "name": "Deductibles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )
    is_included: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsIncluded",
            "type": "Attribute",
        }
    )
    is_custom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCustom",
            "type": "Attribute",
        }
    )
    is_extension: bool = field(
        default=False,
        metadata={
            "name": "IsExtension",
            "type": "Attribute",
        }
    )
