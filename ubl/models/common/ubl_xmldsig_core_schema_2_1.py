from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class CanonicalizationMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"

    p: None | bytes = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    q: None | bytes = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    g: None | bytes = field(
        default=None,
        metadata={
            "name": "G",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    y: bytes = field(
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    j: None | bytes = field(
        default=None,
        metadata={
            "name": "J",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    seed: None | bytes = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )
    pgen_counter: None | bytes = field(
        default=None,
        metadata={
            "name": "PgenCounter",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        },
    )


@dataclass(frozen=True, kw_only=True)
class DigestMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class DigestValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )


@dataclass(frozen=True, kw_only=True)
class KeyName:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class MgmtData:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class ObjectType:
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    mime_type: None | str = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Attribute",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        },
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class PgpdataType:
    class Meta:
        name = "PGPDataType"

    pgpkey_id: bytes = field(
        metadata={
            "name": "PGPKeyID",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    pgpkey_packet: tuple[bytes, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PGPKeyPacket",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
            "format": "base64",
        },
    )
    other_element: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(frozen=True, kw_only=True)
class RsakeyValueType:
    class Meta:
        name = "RSAKeyValueType"

    modulus: bytes = field(
        metadata={
            "name": "Modulus",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    exponent: bytes = field(
        metadata={
            "name": "Exponent",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass(frozen=True, kw_only=True)
class SpkidataType:
    class Meta:
        name = "SPKIDataType"

    spkisexp: tuple[bytes, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SPKISexp",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "sequence": 1,
            "format": "base64",
        },
    )
    other_element: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequence": 1,
        },
    )


@dataclass(frozen=True, kw_only=True)
class SignatureMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "HMACOutputLength",
                    "type": int,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        },
    )


@dataclass(frozen=True, kw_only=True)
class SignaturePropertyType:
    target: str = field(
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(frozen=True, kw_only=True)
class SignatureValueType:
    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class TransformType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "XPath",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        },
    )


@dataclass(frozen=True, kw_only=True)
class X509IssuerSerialType:
    x509_issuer_name: str = field(
        metadata={
            "name": "X509IssuerName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    x509_serial_number: int = field(
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass(frozen=True, kw_only=True)
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Object(ObjectType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignatureProperty(SignaturePropertyType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignatureValue(SignatureValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Transform(TransformType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class X509DataType:
    x509_issuer_serial: tuple[X509IssuerSerialType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequence": 1,
        },
    )
    x509_ski: tuple[bytes, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "X509SKI",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequence": 1,
            "format": "base64",
        },
    )
    x509_subject_name: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "X509SubjectName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequence": 1,
        },
    )
    x509_certificate: tuple[bytes, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequence": 1,
            "format": "base64",
        },
    )
    x509_crl: tuple[bytes, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "X509CRL",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequence": 1,
            "format": "base64",
        },
    )
    other_element: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequence": 1,
        },
    )


@dataclass(frozen=True, kw_only=True)
class KeyValueType:
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        },
    )


@dataclass(frozen=True, kw_only=True)
class SignaturePropertiesType:
    signature_property: tuple[SignatureProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SignatureProperty",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class TransformsType:
    transform: tuple[Transform, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True, kw_only=True)
class X509Data(X509DataType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class KeyValue(KeyValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignatureProperties(SignaturePropertiesType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Transforms(TransformsType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class ReferenceType:
    transforms: None | Transforms = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    digest_method: DigestMethod = field(
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: DigestValue = field(
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class RetrievalMethodType:
    transforms: None | Transforms = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class KeyInfoType:
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    content: tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KeyName",
                    "type": KeyName,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": MgmtData,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        },
    )


@dataclass(frozen=True, kw_only=True)
class ManifestType:
    reference: tuple[Reference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class SignedInfoType:
    canonicalization_method: CanonicalizationMethod = field(
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: SignatureMethod = field(
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: tuple[Reference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class KeyInfo(KeyInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignedInfo(SignedInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass(frozen=True, kw_only=True)
class SignatureType:
    signed_info: SignedInfo = field(
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_value: SignatureValue = field(
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    key_info: None | KeyInfo = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    object_value: tuple[Object, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, kw_only=True)
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
