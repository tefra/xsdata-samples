from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import AllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitution
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitutionBranch
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoiceLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import ItemInstance
from ubl.models.common.ubl_common_aggregate_components_2_1 import LegalMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import LotIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderLineReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PayeeFinancialAccount
from ubl.models.common.ubl_common_aggregate_components_2_1 import PaymentMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import PaymentTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SignatoryParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Signature
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxCategory
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxSubtotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxTotal
from ubl.models.common.ubl_common_basic_components_2_1 import AccountTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import ActualDeliveryDate
from ubl.models.common.ubl_common_basic_components_2_1 import ActualDeliveryTime
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CopyIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import ExpiryDate
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import InvoiceTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import InvoicedQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import LineId
from ubl.models.common.ubl_common_basic_components_2_1 import LineStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import LotNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PaymentDueDate
from ubl.models.common.ubl_common_basic_components_2_1 import PaymentMeansCode
from ubl.models.common.ubl_common_basic_components_2_1 import Percent
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SalesOrderId
from ubl.models.common.ubl_common_basic_components_2_1 import SalesOrderLineId
from ubl.models.common.ubl_common_basic_components_2_1 import SignatureMethod
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplierAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import TaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxEvidenceIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxPointDate
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TaxableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.common.ubl_common_extension_components_2_1 import ExtensionContent
from ubl.models.common.ubl_common_extension_components_2_1 import ExtensionUri
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextension
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions
from ubl.models.common.ubl_common_signature_components_2_1 import UbldocumentSignatures
from ubl.models.common.ubl_signature_aggregate_components_2_1 import SignatureInformation
from ubl.models.common.ubl_xad_esv132_2_1 import AnyType
from ubl.models.common.ubl_xad_esv132_2_1 import QualifyingProperties
from ubl.models.common.ubl_xad_esv132_2_1 import SignedPropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import SignedSignaturePropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import UnsignedPropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import UnsignedSignaturePropertiesType
from ubl.models.common.ubl_xad_esv132_2_1 import XadEstimeStampType
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import CanonicalizationMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import DigestMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import DigestValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import KeyInfo
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import KeyValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Object
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Reference
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import RsakeyValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Signature
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignatureMethod
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignatureValue
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import SignedInfo
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Transform
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import Transforms
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import X509Data
from ubl.models.common.ubl_xmldsig_core_schema_2_1 import X509IssuerSerialType
from ubl.models.maindoc.ubl_invoice_2_1 import Invoice
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Invoice(
    ublextensions=Ublextensions(
        ublextension=[
            Ublextension(
                extension_uri=ExtensionUri(
                    value='dummy1'
                ),
                extension_content=ExtensionContent(
                    other_element=AnyElement(
                        qname='{urn:X-dummy1}AnExtension',
                        text='\n       '
                    )
                )
            ),
            Ublextension(
                extension_uri=ExtensionUri(
                    value='dummy2'
                ),
                extension_content=ExtensionContent(
                    other_element=AnyElement(
                        qname='{urn:X-dummy2}AnotherExtension',
                        text='\n       '
                    )
                )
            ),
            Ublextension(
                extension_content=ExtensionContent(
                    other_element=UbldocumentSignatures(
                        signature_information=[
                            SignatureInformation(
                                signature=Signature(
                                    signed_info=SignedInfo(
                                        canonicalization_method=CanonicalizationMethod(
                                            algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315',
                                            content=[]
                                        ),
                                        signature_method=SignatureMethod(
                                            algorithm='http://www.w3.org/2000/09/xmldsig#rsa-sha1',
                                            content=[]
                                        ),
                                        reference=[
                                            Reference(
                                                transforms=Transforms(
                                                    transform=[
                                                        Transform(
                                                            algorithm='http://www.w3.org/TR/1999/REC-xpath-19991116',
                                                            content=[
                                                                AnyElement(
                                                                    qname='{http://www.w3.org/2000/09/xmldsig#}XPath',
                                                                    text='\n            count(ancestor-or-self::sig:UBLDocumentSignatures |\n                  here()/ancestor::sig:UBLDocumentSignatures[1]) >\n            count(ancestor-or-self::sig:UBLDocumentSignatures)\n          '
                                                                ),
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                digest_method=DigestMethod(
                                                    algorithm='http://www.w3.org/2000/09/xmldsig#sha1',
                                                    content=[]
                                                ),
                                                digest_value=DigestValue(
                                                    value=b'w\xb3\x98\x90\xf1\xf1\xfaO\x90\x83\xebA_d_w6\x81\xb9\x8b'
                                                ),
                                                uri=''
                                            ),
                                            Reference(
                                                digest_method=DigestMethod(
                                                    algorithm='http://www.w3.org/2000/09/xmldsig#sha1',
                                                    content=[]
                                                ),
                                                digest_value=DigestValue(
                                                    value=b'\xad\xc5\xa5R\x81f\xbff\xdeK?!\xe4\x12\xa9\xc4\x1b\xff!d'
                                                ),
                                                uri='#xades-test-s'
                                            ),
                                        ]
                                    ),
                                    signature_value=SignatureValue(
                                        value='nUGjDSgnAizCE4n8VsJhM1DljVf+lmQqKcXiuWkM2xUaRFoni4VUiku7BzC4I8w2\nNbDjhusexvxIzN5IZf8uY4gXn4OrNuWsYZT/U73qj0T8N32jsHpeyXFMsuUq5kgG\nm4MqK4QcI8/VnSYqfGOF/wCJi0GDM/sccLbB7tKgX8Y=',
                                        id='addedSigVal'
                                    ),
                                    key_info=KeyInfo(
                                        content=[
                                            KeyValue(
                                                content=[
                                                    RsakeyValue(
                                                        modulus='\nuXEmg0yTZN1Yf7IuwDcf+MhHjILcPtFXVW3FRFpy5ymWDDmoOddPJrG3S6zHcCbu\nkdqJR+fIHhpGauMifTbC4k9F0UNgT0DSzxoOkVMFwv/pREK28lvnDZD1rGnS9GKt\ncyOMVbGe5BSl49iBI5xhpUtmRYxVR/RAxSUmCrfZFoM=\n',
                                                        exponent='\nAQAB\n'
                                                    ),
                                                ]
                                            ),
                                            X509Data(
                                                x509_issuer_serial=[
                                                    X509IssuerSerialType(
                                                        x509_issuer_name='CN=UBL TC,OU=UBL Technical Committee,O=OASIS,L=Burlington,ST=Massachusetts,C=US',
                                                        x509_serial_number=17517295961972146475
                                                    ),
                                                ],
                                                x509_subject_name=[
                                                    'CN=UBL TC,OU=UBL Technical Committee,O=OASIS,L=Burlington,ST=Massachusetts,C=US',
                                                ],
                                                x509_certificate=[
                                                    'MIICcTCCAdoCCQDzGe/d5rwBKzANBgkqhkiG9w0BAQUFADB9MQswCQYDVQQGEwJV\nUzEWMBQGA1UECAwNTWFzc2FjaHVzZXR0czETMBEGA1UEBwwKQnVybGluZ3RvbjEO\nMAwGA1UECgwFT0FTSVMxIDAeBgNVBAsMF1VCTCBUZWNobmljYWwgQ29tbWl0dGVl\nMQ8wDQYDVQQDDAZVQkwgVEMwHhcNMTMwMjE1MTg1OTQ2WhcNMTMwMzE3MTg1OTQ2\nWjB9MQswCQYDVQQGEwJVUzEWMBQGA1UECAwNTWFzc2FjaHVzZXR0czETMBEGA1UE\nBwwKQnVybGluZ3RvbjEOMAwGA1UECgwFT0FTSVMxIDAeBgNVBAsMF1VCTCBUZWNo\nbmljYWwgQ29tbWl0dGVlMQ8wDQYDVQQDDAZVQkwgVEMwgZ8wDQYJKoZIhvcNAQEB\nBQADgY0AMIGJAoGBALlxJoNMk2TdWH+yLsA3H/jIR4yC3D7RV1VtxURacucplgw5\nqDnXTyaxt0usx3Am7pHaiUfnyB4aRmrjIn02wuJPRdFDYE9A0s8aDpFTBcL/6URC\ntvJb5w2Q9axp0vRirXMjjFWxnuQUpePYgSOcYaVLZkWMVUf0QMUlJgq32RaDAgMB\nAAEwDQYJKoZIhvcNAQEFBQADgYEAVtqeUFJQa64pqCYJAxflCGdOKFBX2p8LCo3K\neupnQC9UvLdOxuS8fAjzo40FQG687/7NGcZ30ysVjy/s3XyqxDFLln601vI470i9\n6Gip3cBF8WHB5lUnvaT9dNEYFDBBR22glEnY9SA8y8EbbO+Cy8hIQEzULoVOkr/a\nJfeH5w4=',
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
                                                        id='xades-test-s'
                                                    ),
                                                    unsigned_properties=UnsignedPropertiesType(
                                                        unsigned_signature_properties=UnsignedSignaturePropertiesType(
                                                            signature_time_stamp=[
                                                                XadEstimeStampType(
                                                                    xmltime_stamp=[
                                                                        AnyType(
                                                                            content=[
                                                                                '2010-11-26T18:00:00Z',
                                                                            ]
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                        id='xades-test-u'
                                                    ),
                                                    target='#addedSig'
                                                ),
                                            ]
                                        ),
                                    ],
                                    id='addedSig'
                                )
                            ),
                        ]
                    )
                )
            ),
        ]
    ),
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:Invoice-2.0:sbs-1.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-invoice-notification-draft'
    ),
    id=Id(
        value='A00095678'
    ),
    copy_indicator=CopyIndicator(
        value=False
    ),
    uuid=Uuid(
        value='849FBBCE-E081-40B4-906C-94C5FF9D1AC3'
    ),
    issue_date=IssueDate(
        value=XmlDate(2005, 6, 21)
    ),
    invoice_type_code=InvoiceTypeCode(
        value='SalesInvoice'
    ),
    note=[
        Note(
            value='sample'
        ),
    ],
    tax_point_date=TaxPointDate(
        value=XmlDate(2005, 6, 21)
    ),
    order_reference=OrderReference(
        id=Id(
            value='AEG012345'
        ),
        sales_order_id=SalesOrderId(
            value='CON0095678'
        ),
        uuid=Uuid(
            value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
        ),
        issue_date=IssueDate(
            value=XmlDate(2005, 6, 20)
        )
    ),
    signature=[
        Signature(
            id=Id(
                value='urn:oasis:names:specification:ubl:signature:Invoice'
            ),
            signature_method=SignatureMethod(
                value='urn:oasis:names:specification:ubl:dsig:enveloped'
            ),
            signatory_party=SignatoryParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value='MyParty'
                        )
                    ),
                ]
            )
        ),
    ],
    accounting_supplier_party=AccountingSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value='CO001'
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='Consortial'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Busy Street'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Farthing'
                ),
                postal_zone=PostalZone(
                    value='AA99 1BB'
                ),
                country_subentity=CountrySubentity(
                    value='Heremouthshire'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='The Roundabout'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value='Farthing Purchasing Consortium'
                    ),
                    company_id=CompanyId(
                        value='175 269 2355'
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value='N/A'
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='VAT'
                        ),
                        tax_type_code=TaxTypeCode(
                            value='VAT'
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value='Mrs Bouquet'
                ),
                telephone=Telephone(
                    value='0158 1233714'
                ),
                telefax=Telefax(
                    value='0158 1233856'
                ),
                electronic_mail=ElectronicMail(
                    value='bouquet@fpconsortial.co.uk'
                )
            )
        )
    ),
    accounting_customer_party=AccountingCustomerParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value='XFB01'
        ),
        supplier_assigned_account_id=SupplierAssignedAccountId(
            value='GT00978567'
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='IYT Corporation'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value='Bridgtow District Council'
                    ),
                    company_id=CompanyId(
                        value='12356478'
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value='Local Authority'
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='UK VAT'
                        ),
                        tax_type_code=TaxTypeCode(
                            value='VAT'
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value='Mr Fred Churchill'
                ),
                telephone=Telephone(
                    value='0127 2653214'
                ),
                telefax=Telefax(
                    value='0127 2653215'
                ),
                electronic_mail=ElectronicMail(
                    value='fred@iytcorporation.gov.uk'
                )
            )
        )
    ),
    delivery=[
        Delivery(
            actual_delivery_date=ActualDeliveryDate(
                value=XmlDate(2005, 6, 20)
            ),
            actual_delivery_time=ActualDeliveryTime(
                value=XmlTime(11, 30, 0, 0, 0)
            ),
            delivery_address=DeliveryAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            )
        ),
    ],
    payment_means=[
        PaymentMeans(
            payment_means_code=PaymentMeansCode(
                value='20'
            ),
            payment_due_date=PaymentDueDate(
                value=XmlDate(2005, 7, 21)
            ),
            payee_financial_account=PayeeFinancialAccount(
                id=Id(
                    value='12345678'
                ),
                name=Name(
                    value='Farthing Purchasing Consortium'
                ),
                account_type_code=AccountTypeCode(
                    value='Current'
                ),
                currency_code=CurrencyCode(
                    value='GBP'
                ),
                financial_institution_branch=FinancialInstitutionBranch(
                    id=Id(
                        value='10-26-58'
                    ),
                    name=Name(
                        value='Open Bank Ltd, Bridgstow Branch '
                    ),
                    financial_institution=FinancialInstitution(
                        id=Id(
                            value='10-26-58'
                        ),
                        name=Name(
                            value='Open Bank Ltd'
                        ),
                        address=Address(
                            street_name=StreetName(
                                value='City Road'
                            ),
                            building_name=BuildingName(
                                value='Banking House'
                            ),
                            building_number=BuildingNumber(
                                value='12'
                            ),
                            city_name=CityName(
                                value='London'
                            ),
                            postal_zone=PostalZone(
                                value='AQ1 6TH'
                            ),
                            country_subentity=CountrySubentity(
                                value='London\n'
                            ),
                            address_line=[
                                AddressLine(
                                    line=Line(
                                        value='5th Floor'
                                    )
                                ),
                            ],
                            country=Country(
                                identification_code=IdentificationCode(
                                    value='GB'
                                )
                            )
                        )
                    ),
                    address=Address(
                        street_name=StreetName(
                            value='Busy Street'
                        ),
                        building_name=BuildingName(
                            value='The Mall'
                        ),
                        building_number=BuildingNumber(
                            value='152'
                        ),
                        city_name=CityName(
                            value='Farthing'
                        ),
                        postal_zone=PostalZone(
                            value='AA99 1BB'
                        ),
                        country_subentity=CountrySubentity(
                            value='Heremouthshire'
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value='West Wing'
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value='GB'
                            )
                        )
                    )
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            )
        ),
    ],
    payment_terms=[
        PaymentTerms(
            note=[
                Note(
                    value='Payable within 1 calendar month from the invoice date'
                ),
            ]
        ),
    ],
    allowance_charge=[
        AllowanceCharge(
            charge_indicator=ChargeIndicator(
                value=False
            ),
            allowance_charge_reason_code=AllowanceChargeReasonCode(
                value='17'
            ),
            multiplier_factor_numeric=MultiplierFactorNumeric(
                value=Decimal('0.10')
            ),
            amount=Amount(
                value=Decimal('10.00'),
                currency_id='GBP'
            )
        ),
    ],
    tax_total=[
        TaxTotal(
            tax_amount=TaxAmount(
                value=Decimal('17.50'),
                currency_id='GBP'
            ),
            tax_evidence_indicator=TaxEvidenceIndicator(
                value=True
            ),
            tax_subtotal=[
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal('100.00'),
                        currency_id='GBP'
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal('17.50'),
                        currency_id='GBP'
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value='A'
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value='UK VAT'
                            ),
                            tax_type_code=TaxTypeCode(
                                value='VAT'
                            )
                        )
                    )
                ),
            ]
        ),
    ],
    legal_monetary_total=LegalMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal('100.00'),
            currency_id='GBP'
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal('90.00'),
            currency_id='GBP'
        ),
        allowance_total_amount=AllowanceTotalAmount(
            value=Decimal('10.00'),
            currency_id='GBP'
        ),
        payable_amount=PayableAmount(
            value=Decimal('107.50'),
            currency_id='GBP'
        )
    ),
    invoice_line=[
        InvoiceLine(
            id=Id(
                value='A'
            ),
            invoiced_quantity=InvoicedQuantity(
                value=Decimal('100'),
                unit_code='KGM'
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal('100.00'),
                currency_id='GBP'
            ),
            order_line_reference=[
                OrderLineReference(
                    line_id=LineId(
                        value='1'
                    ),
                    sales_order_line_id=SalesOrderLineId(
                        value='A'
                    ),
                    line_status_code=LineStatusCode(
                        value='NoStatus'
                    ),
                    order_reference=OrderReference(
                        id=Id(
                            value='AEG012345'
                        ),
                        sales_order_id=SalesOrderId(
                            value='CON0095678'
                        ),
                        uuid=Uuid(
                            value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
                        ),
                        issue_date=IssueDate(
                            value=XmlDate(2005, 6, 20)
                        )
                    )
                ),
            ],
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal('17.50'),
                        currency_id='GBP'
                    ),
                    tax_evidence_indicator=TaxEvidenceIndicator(
                        value=True
                    ),
                    tax_subtotal=[
                        TaxSubtotal(
                            taxable_amount=TaxableAmount(
                                value=Decimal('100.00'),
                                currency_id='GBP'
                            ),
                            tax_amount=TaxAmount(
                                value=Decimal('17.50'),
                                currency_id='GBP'
                            ),
                            tax_category=TaxCategory(
                                id=Id(
                                    value='A'
                                ),
                                percent=Percent(
                                    value=Decimal('17.5')
                                ),
                                tax_scheme=TaxScheme(
                                    id=Id(
                                        value='UK VAT'
                                    ),
                                    tax_type_code=TaxTypeCode(
                                        value='VAT'
                                    )
                                )
                            )
                        ),
                    ]
                ),
            ],
            item=Item(
                description=[
                    Description(
                        value='Acme beeswax'
                    ),
                ],
                name=Name(
                    value='beeswax'
                ),
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='6578489'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='17589683'
                    )
                ),
                item_instance=[
                    ItemInstance(
                        lot_identification=LotIdentification(
                            lot_number_id=LotNumberId(
                                value='546378239'
                            ),
                            expiry_date=ExpiryDate(
                                value=XmlDate(2010, 1, 1)
                            )
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal('1.00'),
                    currency_id='GBP'
                ),
                base_quantity=BaseQuantity(
                    value=Decimal('1'),
                    unit_code='KGM'
                )
            )
        ),
    ]
)
