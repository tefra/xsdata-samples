from dataclasses import dataclass, field

from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_signature_basic_components_2_1 import (
    ReferencedSignatureId,
)
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Signature

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2"


@dataclass(frozen=True)
class SignatureInformationType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    referenced_signature_id: ReferencedSignatureId | None = field(
        default=None,
        metadata={
            "name": "ReferencedSignatureID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2",
        },
    )
    signature: Signature | None = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass(frozen=True)
class SignatureInformation(SignatureInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2"
