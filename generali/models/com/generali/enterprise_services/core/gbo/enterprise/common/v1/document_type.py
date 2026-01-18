from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class DocumentType(BaseReferenceComponentType):
    note: None | str = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    document_location: None | str = field(
        default=None,
        metadata={
            "name": "DocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    file_type: None | str = field(
        default=None,
        metadata={
            "name": "FileType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    author: None | TextType = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    doc_type: None | TextType = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    local_policy_ref: None | TextType = field(
        default=None,
        metadata={
            "name": "LocalPolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    issue_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    producing_office_ref: None | TextType = field(
        default=None,
        metadata={
            "name": "ProducingOfficeRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    additional_information: None | TextType = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    cdmsdocument_location: None | str = field(
        default=None,
        metadata={
            "name": "CDMSDocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    reinsurance_policy_ref: None | TextType = field(
        default=None,
        metadata={
            "name": "ReinsurancePolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
