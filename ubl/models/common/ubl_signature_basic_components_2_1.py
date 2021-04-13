from dataclasses import dataclass
from ubl.models.common.ubl_unqualified_data_types_2_1 import IdentifierType

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2"


@dataclass
class ReferencedSignatureIdtype(IdentifierType):
    class Meta:
        name = "ReferencedSignatureIDType"


@dataclass
class ReferencedSignatureId(ReferencedSignatureIdtype):
    class Meta:
        name = "ReferencedSignatureID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2"
