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
from xsdata.formats.dataclass.models.generics import AnyElement


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
        value=b"VH\x95\x10\x89\x0fL\x84\xab\xaf\x07E\xa2\xe5\xd6\x10x\xab\xc5$\xf6\x98&\xcb\xb9y\xa0;D\xfe\xe1E\xc7\xab\xd4\xa2\xaf\xef\xfd\x82q\x19S\xb0\x1a\xd8\xf0\x81C\xfd\xd7\xd1\x12$_\xfb\x10\xc0c\ru\x0ecP\x95\x9c\xd0\x1a\x06:\xcc\xe1s@\x98\x1f\x10\xe2k*\xa5C\x87\xd9\x1b?\xa7\x85WhR\x888\xa3\xb4\xf1vO\xaf\xbb\xf2\xd2\xff\xb8\xb3\xe9\xab.uzvf\x1f-O\x82\xe78\x83l\x8f\xef\xff\r\xd4]\xeb#",
        id="addedSigVal"
    ),
    key_info=KeyInfo(
        content=[
            KeyValue(
                content=[
                    RsakeyValue(
                        modulus=b"\xb9q&\x83L\x93d\xddX\x7f\xb2.\xc07\x1f\xf8\xc8G\x8c\x82\xdc>\xd1WUm\xc5DZr\xe7)\x96\x0c9\xa89\xd7O&\xb1\xb7K\xac\xc7p&\xee\x91\xda\x89G\xe7\xc8\x1e\x1aFj\xe3"}6\xc2\xe2OE\xd1C`O@\xd2\xcf\x1a\x0e\x91S\x05\xc2\xff\xe9DB\xb6\xf2[\xe7\r\x90\xf5\xaci\xd2\xf4b\xads#\x8cU\xb1\x9e\xe4\x14\xa5\xe3\xd8\x81#\x9ca\xa5KfE\x8cUG\xf4@\xc5%&\n\xb7\xd9\x16\x83",
                        exponent=b"\x01\x00\x01"
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
                    b"0\x82\x02q0\x82\x01\xda\x02\t\x00\xf3\x19\xef\xdd\xe6\xbc\x01+0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x05\x05\x000}1\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x160\x14\x06\x03U\x04\x08\x0c\rMassachusetts1\x130\x11\x06\x03U\x04\x07\x0c\nBurlington1\x0e0\x0c\x06\x03U\x04\n\x0c\x05OASIS1 0\x1e\x06\x03U\x04\x0b\x0c\x17UBL Technical Committee1\x0f0\r\x06\x03U\x04\x03\x0c\x06UBL TC0\x1e\x17\r130215185946Z\x17\r130317185946Z0}1\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x160\x14\x06\x03U\x04\x08\x0c\rMassachusetts1\x130\x11\x06\x03U\x04\x07\x0c\nBurlington1\x0e0\x0c\x06\x03U\x04\n\x0c\x05OASIS1 0\x1e\x06\x03U\x04\x0b\x0c\x17UBL Technical Committee1\x0f0\r\x06\x03U\x04\x03\x0c\x06UBL TC0\x81\x9f0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x81\x8d\x000\x81\x89\x02\x81\x81\x00\xb9q&\x83L\x93d\xddX\x7f\xb2.\xc07\x1f\xf8\xc8G\x8c\x82\xdc>\xd1WUm\xc5DZr\xe7)\x96\x0c9\xa89\xd7O&\xb1\xb7K\xac\xc7p&\xee\x91\xda\x89G\xe7\xc8\x1e\x1aFj\xe3"}6\xc2\xe2OE\xd1C`O@\xd2\xcf\x1a\x0e\x91S\x05\xc2\xff\xe9DB\xb6\xf2[\xe7\r\x90\xf5\xaci\xd2\xf4b\xads#\x8cU\xb1\x9e\xe4\x14\xa5\xe3\xd8\x81#\x9ca\xa5KfE\x8cUG\xf4@\xc5%&\n\xb7\xd9\x16\x83\x02\x03\x01\x00\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x05\x05\x00\x03\x81\x81\x00V\xda\x9ePRPk\xae)\xa8&\t\x03\x17\xe5\x08gN(PW\xda\x9f\x0b\n\x8d\xcaz\xeag@/T\xbc\xb7N\xc6\xe4\xbc|\x08\xf3\xa3\x8d\x05@n\xbc\xef\xfe\xcd\x19\xc6w\xd3+\x15\x8f/\xec\xdd|\xaa\xc41K\x96~\xb4\xd6\xf28\xefH\xbd\xe8h\xa9\xdd\xc0E\xf1a\xc1\xe6U\"\xbd\xa4\xfdt\xd1\x18\x140AGm\xa0\x94I\xd8\xf5 <\xcb\xc1\x1bl\xef\x82\xcb\xc8H@L\xd4.\x85N\x92\xbf\xda%\xf7\x87\xe7\x0e",
                ]
            ),
        ]
    ),
    object_value=[
        Object(
            content=[
                AnyElement(
                    qname="{http://uri.etsi.org/01903/v1.3.2#}QualifyingProperties",
                    text="",
                    children=[
                        AnyElement(
                            qname="{http://uri.etsi.org/01903/v1.3.2#}SignedProperties",
                            text="",
                            children=[
                                AnyElement(
                                    qname="{http://uri.etsi.org/01903/v1.3.2#}SignedSignatureProperties",
                                    text="",
                                    children=[
                                        AnyElement(
                                            qname="{http://uri.etsi.org/01903/v1.3.2#}SigningTime",
                                            text="2010-11-26T18:00:00Z"
                                        ),
                                    ]
                                ),
                            ],
                            attributes={
                                "Id": "xades-test-s",
                            }
                        ),
                        AnyElement(
                            qname="{http://uri.etsi.org/01903/v1.3.2#}UnsignedProperties",
                            text="",
                            children=[
                                AnyElement(
                                    qname="{http://uri.etsi.org/01903/v1.3.2#}UnsignedSignatureProperties",
                                    text="",
                                    children=[
                                        AnyElement(
                                            qname="{http://uri.etsi.org/01903/v1.3.2#}SignatureTimeStamp",
                                            text="",
                                            children=[
                                                AnyElement(
                                                    qname="{http://uri.etsi.org/01903/v1.3.2#}XMLTimeStamp",
                                                    text="2010-11-26T18:00:00Z"
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            attributes={
                                "Id": "xades-test-u",
                            }
                        ),
                    ],
                    attributes={
                        "Target": "#addedSig",
                    }
                ),
            ]
        ),
    ],
    id="addedSig"
)
