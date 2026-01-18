from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import (
    BaseReferenceComponentType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class DocumentType(BaseReferenceComponentType):
    note: str | None = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    document_location: str | None = field(
        default=None,
        metadata={
            "name": "DocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    file_type: str | None = field(
        default=None,
        metadata={
            "name": "FileType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    author: TextType | None = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    doc_type: TextType | None = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    local_policy_ref: TextType | None = field(
        default=None,
        metadata={
            "name": "LocalPolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    issue_date: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    producing_office_ref: TextType | None = field(
        default=None,
        metadata={
            "name": "ProducingOfficeRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    additional_information: TextType | None = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    cdmsdocument_location: str | None = field(
        default=None,
        metadata={
            "name": "CDMSDocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    reinsurance_policy_ref: TextType | None = field(
        default=None,
        metadata={
            "name": "ReinsurancePolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
