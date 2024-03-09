from dataclasses import dataclass, field
from typing import Tuple

from ubl.models.common.ubl_signature_aggregate_components_2_1 import (
    SignatureInformation,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2"
)


@dataclass(frozen=True)
class UbldocumentSignaturesType:
    class Meta:
        name = "UBLDocumentSignaturesType"

    signature_information: Tuple[SignatureInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SignatureInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:SignatureAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class UbldocumentSignatures(UbldocumentSignaturesType):
    class Meta:
        name = "UBLDocumentSignatures"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonSignatureComponents-2"
