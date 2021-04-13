from dataclasses import dataclass, field
from typing import List
from ubl.models.common.ubl_signature_aggregate_components_2_1 import SignatureInformation

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2"


@dataclass
class UbldocumentSignaturesType:
    class Meta:
        name = "UBLDocumentSignaturesType"

    signature_information: List[SignatureInformation] = field(
        default_factory=list,
        metadata={
            "name": "SignatureInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class UbldocumentSignatures(UbldocumentSignaturesType):
    class Meta:
        name = "UBLDocumentSignatures"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2"
