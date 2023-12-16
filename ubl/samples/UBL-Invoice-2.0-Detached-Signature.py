from ubl.models.common.ubl_xad_esv132_2_1 import AnyType
from ubl.models.common.ubl_xad_esv132_2_1 import QualifyingProperties
from ubl.models.common.ubl_xad_esv132_2_1 import SignedPropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import SignedSignaturePropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import UnsignedPropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import UnsignedSignaturePropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import XadEstimeStampType
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import CanonicalizationMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import DigestMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import KeyInfo
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import KeyValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Object
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Reference
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import RsakeyValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Signature
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignatureMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignatureValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignedInfo
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import X509Data
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import X509IssuerSerialType
from xsdata.models.datatype import XmlDateTime


obj = Signature(
    signed_info=SignedInfo(
        canonicalization_method=CanonicalizationMethod(
            algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
            content=[]
        ),
        signature_method=SignatureMethod(
            algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1",
            content=[]
        ),
        reference=[
            Reference(
                digest_method=DigestMethod(
                    algorithm="http://www.w3.org/2000/09/xmldsig#sha1",
                    content=[]
                ),
                digest_value=b"\xa8\xcf\xfe\x1a\xc88\xfcO\xf4\xa7w\xc4\xf4\xb4\xd9\x03\xa5\xed\x91\xdb",
                uri="UBL-Invoice-2.0-Detached.xml"
            ),
            Reference(
                digest_method=DigestMethod(
                    algorithm="http://www.w3.org/2000/09/xmldsig#sha1",
                    content=[]
                ),
                digest_value=b"\x9a8\x91\xeb[K\xd9\xd5w\x1c\xcb\xac\xdc`F\xfd\xa1#n\xde",
                uri="#xades-test-s"
            ),
        ]
    ),
    signature_value=SignatureValue(
        value="VkiVEIkPTISrrwdFouXWEHirxST2mCbLuXmgO0T+4UXHq9Sir+/9gnEZU7Aa2PCB\nQ/3X0RIkX/sQwGMNdQ5jUJWc0BoGOszhc0CYHxDiayqlQ4fZGz+nhVdoUog4o7Tx\ndk+vu/LS/7iz6asudXp2Zh8tT4LnOINsj+//DdRd6yM=",
        id="addedSigVal"
    ),
    key_info=KeyInfo(
        content=[
            KeyValue(
                content=[
                    RsakeyValue(
                        modulus="\nuXEmg0yTZN1Yf7IuwDcf+MhHjILcPtFXVW3FRFpy5ymWDDmoOddPJrG3S6zHcCbu\nkdqJR+fIHhpGauMifTbC4k9F0UNgT0DSzxoOkVMFwv/pREK28lvnDZD1rGnS9GKt\ncyOMVbGe5BSl49iBI5xhpUtmRYxVR/RAxSUmCrfZFoM=\n",
                        exponent="\nAQAB\n"
                    ),
                ]
            ),
            X509Data(
                x509_issuer_serial=[
                    X509IssuerSerialType(
                        x509_issuer_name="CN=UBL TC,OU=UBL Technical Committee,O=OASIS,L=Burlington,ST=Massachusetts,C=US",
                        x509_serial_number=17517295961972146475
                    ),
                ],
                x509_subject_name=[
                    "CN=UBL TC,OU=UBL Technical Committee,O=OASIS,L=Burlington,ST=Massachusetts,C=US",
                ],
                x509_certificate=[
                    "MIICcTCCAdoCCQDzGe/d5rwBKzANBgkqhkiG9w0BAQUFADB9MQswCQYDVQQGEwJV\nUzEWMBQGA1UECAwNTWFzc2FjaHVzZXR0czETMBEGA1UEBwwKQnVybGluZ3RvbjEO\nMAwGA1UECgwFT0FTSVMxIDAeBgNVBAsMF1VCTCBUZWNobmljYWwgQ29tbWl0dGVl\nMQ8wDQYDVQQDDAZVQkwgVEMwHhcNMTMwMjE1MTg1OTQ2WhcNMTMwMzE3MTg1OTQ2\nWjB9MQswCQYDVQQGEwJVUzEWMBQGA1UECAwNTWFzc2FjaHVzZXR0czETMBEGA1UE\nBwwKQnVybGluZ3RvbjEOMAwGA1UECgwFT0FTSVMxIDAeBgNVBAsMF1VCTCBUZWNo\nbmljYWwgQ29tbWl0dGVlMQ8wDQYDVQQDDAZVQkwgVEMwgZ8wDQYJKoZIhvcNAQEB\nBQADgY0AMIGJAoGBALlxJoNMk2TdWH+yLsA3H/jIR4yC3D7RV1VtxURacucplgw5\nqDnXTyaxt0usx3Am7pHaiUfnyB4aRmrjIn02wuJPRdFDYE9A0s8aDpFTBcL/6URC\ntvJb5w2Q9axp0vRirXMjjFWxnuQUpePYgSOcYaVLZkWMVUf0QMUlJgq32RaDAgMB\nAAEwDQYJKoZIhvcNAQEFBQADgYEAVtqeUFJQa64pqCYJAxflCGdOKFBX2p8LCo3K\neupnQC9UvLdOxuS8fAjzo40FQG687/7NGcZ30ysVjy/s3XyqxDFLln601vI470i9\n6Gip3cBF8WHB5lUnvaT9dNEYFDBBR22glEnY9SA8y8EbbO+Cy8hIQEzULoVOkr/a\nJfeH5w4=",
                ]
            ),
        ]
    ),
    object_value=[
        Object(
            content=[
                QualifyingProperties(
                    signed_properties=SignedPropertiesType(
                        signed_signature_properties=SignedSignaturePropertiesType(
                            signing_time=XmlDateTime(2010, 11, 26, 18, 0, 0, 0, 0)
                        ),
                        id="xades-test-s"
                    ),
                    unsigned_properties=UnsignedPropertiesType(
                        unsigned_signature_properties=UnsignedSignaturePropertiesType(
                            signature_time_stamp=[
                                XadEstimeStampType(
                                    xmltime_stamp=[
                                        AnyType(
                                            content=[
                                                "2010-11-26T18:00:00Z",
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        id="xades-test-u"
                    ),
                    target="#addedSig"
                ),
            ]
        ),
    ],
    id="addedSig"
)
