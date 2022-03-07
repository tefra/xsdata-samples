from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gboroles_type import BaseGborolesType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class OrganisationRoleType(BaseGborolesType):
    """
    :ivar legal_name: The legal name of the Organisation
    :ivar gunsnumber: The Generali Universal Numbering System,
        abbreviated as GUNS, is the unique identifier assigned by
        Generali to a single business entity held in the Business
        Partner Repository (BPR).
    :ivar dunsnumber: The Generali Universal Numbering System,
        abbreviated as GUNS, is the unique identifier assigned by
        Generali to a single business entity held in the Business
        Partner Repository (BPR).
    """
    legal_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    gunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        }
    )
    dunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "length": 9,
            "pattern": r"([0-9]{9})",
        }
    )
