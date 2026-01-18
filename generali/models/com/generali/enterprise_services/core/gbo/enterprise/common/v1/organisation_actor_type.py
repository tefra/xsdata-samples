from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class OrganisationActorType(BaseComponentType):
    """
    <description xmlns="">The definition of an Organisation parties basic
    details</description>.

    :ivar legal_name: The legal name of the Organisation
    :ivar gunsnumber: The Generali Universal Numbering System,
        abbreviated as GUNS, is the unique identifier assigned by
        Generali to a single business entity held in the Business
        Partner Repository (BPR).
    :ivar dunsnumber: The D&amp;B Universal Numbering System,
        abbreviated as DUNS, is the unique identifier assigned by
        D&amp;B.
    :ivar national_id:
    """

    legal_name: None | TextType = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
    gunsnumber: None | str = field(
        default=None,
        metadata={
            "name": "GUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    dunsnumber: None | str = field(
        default=None,
        metadata={
            "name": "DUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    national_id: None | Idtype = field(
        default=None,
        metadata={
            "name": "NationalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        },
    )
