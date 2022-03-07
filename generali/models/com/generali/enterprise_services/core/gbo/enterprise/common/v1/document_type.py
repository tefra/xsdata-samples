from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import BaseReferenceComponentType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


@dataclass
class DocumentType(BaseReferenceComponentType):
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    document_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    author: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    doc_type: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "DocType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    local_policy_ref: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LocalPolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    issue_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    producing_office_ref: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ProducingOfficeRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    additional_information: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    cdmsdocument_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CDMSDocumentLocation",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
    reinsurance_policy_ref: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ReinsurancePolicyRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        }
    )
