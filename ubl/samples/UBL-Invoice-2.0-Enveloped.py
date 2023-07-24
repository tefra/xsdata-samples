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
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import InvoiceTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import InvoicedQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import LineId
from ubl.models.common.ubl_common_basic_components_2_1 import LineStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import LotNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
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
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
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
                    value="dummy1"
                ),
                extension_content=ExtensionContent(
                    other_element=AnyElement(
                        qname="{urn:X-dummy1}AnExtension",
                        text="&#10;       "
                    )
                )
            ),
            Ublextension(
                extension_uri=ExtensionUri(
                    value="dummy2"
                ),
                extension_content=ExtensionContent(
                    other_element=AnyElement(
                        qname="{urn:X-dummy2}AnotherExtension",
                        text="&#10;       "
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
                                            algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
                                            content=[]
                                        ),
                                        signature_method=SignatureMethod(
                                            algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1",
                                            content=[]
                                        ),
                                        reference=[
                                            Reference(
                                                transforms=Transforms(
                                                    transform=[
                                                        Transform(
                                                            algorithm="http://www.w3.org/TR/1999/REC-xpath-19991116",
                                                            content=[
                                                                AnyElement(
                                                                    qname="{http://www.w3.org/2000/09/xmldsig#}XPath",
                                                                    text="&#10;            count(ancestor-or-self::sig:UBLDocumentSignatures |&#10;                  here()/ancestor::sig:UBLDocumentSignatures[1]) &gt;&#10;            count(ancestor-or-self::sig:UBLDocumentSignatures)&#10;          "
                                                                ),
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                digest_method=DigestMethod(
                                                    algorithm="http://www.w3.org/2000/09/xmldsig#sha1",
                                                    content=[]
                                                ),
                                                digest_value=b"w\xb3\x98\x90\xf1\xf1\xfaO\x90\x83\xebA_d_w6\x81\xb9\x8b",
                                                uri=""
                                            ),
                                            Reference(
                                                digest_method=DigestMethod(
                                                    algorithm="http://www.w3.org/2000/09/xmldsig#sha1",
                                                    content=[]
                                                ),
                                                digest_value=b"\xad\xc5\xa5R\x81f\xbff\xdeK?!\xe4\x12\xa9\xc4\x1b\xff!d",
                                                uri="#xades-test-s"
                                            ),
                                        ]
                                    ),
                                    signature_value=SignatureValue(
                                        value=b"\x9dA\xa3\r("\x02,\xc2\x13\x89\xfcV\xc2a3P\xe5\x8dW\xfe\x96d*)\xc5\xe2\xb9i\x0c\xdb\x15\x1aDZ"\x8b\x85T\x8aK\xbb\x070\xb8#\xcc65\xb0\xe3\x86\xeb\x1e\xc6\xfcH\xcc\xdeHe\xff.c\x88\x17\x9f\x83\xab6\xe5\xaca\x94\xffS\xbd\xea\x8fD\xfc7}\xa3\xb0z^\xc9qL\xb2\xe5*\xe6H\x06\x9b\x83*+\x84\x1c#\xcf\xd5\x9d&*|c\x85\xff\x00\x89\x8bA\x833\xfb\x1cp\xb6\xc1\xee\xd2\xa0_\xc6",
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
                            ),
                        ]
                    )
                )
            ),
        ]
    ),
    ublversion_id=UblversionId(
        value="2.0"
    ),
    customization_id=CustomizationId(
        value="urn:oasis:names:specification:ubl:xpath:Invoice-2.0:sbs-1.0-draft"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-invoice-notification-draft"
    ),
    id=Id(
        value="A00095678"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="849FBBCE-E081-40B4-906C-94C5FF9D1AC3"
    ),
    issue_date=XmlDate(2005, 6, 21),
    invoice_type_code=InvoiceTypeCode(
        value="SalesInvoice"
    ),
    note=[
        Note(
            value="sample"
        ),
    ],
    tax_point_date=XmlDate(2005, 6, 21),
    order_reference=OrderReference(
        id=Id(
            value="AEG012345"
        ),
        sales_order_id=SalesOrderId(
            value="CON0095678"
        ),
        uuid=Uuid(
            value="6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1"
        ),
        issue_date=XmlDate(2005, 6, 20)
    ),
    signature=[
        Signature(
            id=Id(
                value="urn:oasis:names:specification:ubl:signature:Invoice"
            ),
            signature_method=SignatureMethod(
                value="urn:oasis:names:specification:ubl:dsig:enveloped"
            ),
            signatory_party=SignatoryParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value="MyParty"
                        )
                    ),
                ]
            )
        ),
    ],
    accounting_supplier_party=AccountingSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value="CO001"
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="Consortial"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Busy Street"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Farthing"
                ),
                postal_zone=PostalZone(
                    value="AA99 1BB"
                ),
                country_subentity=CountrySubentity(
                    value="Heremouthshire"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="The Roundabout"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value="Farthing Purchasing Consortium"
                    ),
                    company_id=CompanyId(
                        value="175 269 2355"
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value="N/A"
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="VAT"
                        ),
                        tax_type_code=TaxTypeCode(
                            value="VAT"
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value="Mrs Bouquet"
                ),
                telephone=Telephone(
                    value="0158 1233714"
                ),
                telefax=Telefax(
                    value="0158 1233856"
                ),
                electronic_mail=ElectronicMail(
                    value="bouquet@fpconsortial.co.uk"
                )
            )
        )
    ),
    accounting_customer_party=AccountingCustomerParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value="XFB01"
        ),
        supplier_assigned_account_id=SupplierAssignedAccountId(
            value="GT00978567"
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="IYT Corporation"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Avon Way"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Bridgtow"
                ),
                postal_zone=PostalZone(
                    value="ZZ99 1ZZ"
                ),
                country_subentity=CountrySubentity(
                    value="Avon"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="3rd Floor, Room 5"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value="Bridgtow District Council"
                    ),
                    company_id=CompanyId(
                        value="12356478"
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value="Local Authority"
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="UK VAT"
                        ),
                        tax_type_code=TaxTypeCode(
                            value="VAT"
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value="Mr Fred Churchill"
                ),
                telephone=Telephone(
                    value="0127 2653214"
                ),
                telefax=Telefax(
                    value="0127 2653215"
                ),
                electronic_mail=ElectronicMail(
                    value="fred@iytcorporation.gov.uk"
                )
            )
        )
    ),
    delivery=[
        Delivery(
            actual_delivery_date=XmlDate(2005, 6, 20),
            actual_delivery_time=XmlTime(11, 30, 0, 0, 0),
            delivery_address=DeliveryAddress(
                street_name=StreetName(
                    value="Avon Way"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Bridgtow"
                ),
                postal_zone=PostalZone(
                    value="ZZ99 1ZZ"
                ),
                country_subentity=CountrySubentity(
                    value="Avon"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="3rd Floor, Room 5"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            )
        ),
    ],
    payment_means=[
        PaymentMeans(
            payment_means_code=PaymentMeansCode(
                value="20"
            ),
            payment_due_date=XmlDate(2005, 7, 21),
            payee_financial_account=PayeeFinancialAccount(
                id=Id(
                    value="12345678"
                ),
                name=Name(
                    value="Farthing Purchasing Consortium"
                ),
                account_type_code=AccountTypeCode(
                    value="Current"
                ),
                currency_code=CurrencyCode(
                    value="GBP"
                ),
                financial_institution_branch=FinancialInstitutionBranch(
                    id=Id(
                        value="10-26-58"
                    ),
                    name=Name(
                        value="Open Bank Ltd, Bridgstow Branch "
                    ),
                    financial_institution=FinancialInstitution(
                        id=Id(
                            value="10-26-58"
                        ),
                        name=Name(
                            value="Open Bank Ltd"
                        ),
                        address=Address(
                            street_name=StreetName(
                                value="City Road"
                            ),
                            building_name=BuildingName(
                                value="Banking House"
                            ),
                            building_number=BuildingNumber(
                                value="12"
                            ),
                            city_name=CityName(
                                value="London"
                            ),
                            postal_zone=PostalZone(
                                value="AQ1 6TH"
                            ),
                            country_subentity=CountrySubentity(
                                value="London&#10;"
                            ),
                            address_line=[
                                AddressLine(
                                    line=Line(
                                        value="5th Floor"
                                    )
                                ),
                            ],
                            country=Country(
                                identification_code=IdentificationCode(
                                    value="GB"
                                )
                            )
                        )
                    ),
                    address=Address(
                        street_name=StreetName(
                            value="Busy Street"
                        ),
                        building_name=BuildingName(
                            value="The Mall"
                        ),
                        building_number=BuildingNumber(
                            value="152"
                        ),
                        city_name=CityName(
                            value="Farthing"
                        ),
                        postal_zone=PostalZone(
                            value="AA99 1BB"
                        ),
                        country_subentity=CountrySubentity(
                            value="Heremouthshire"
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value="West Wing"
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value="GB"
                            )
                        )
                    )
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            )
        ),
    ],
    payment_terms=[
        PaymentTerms(
            note=[
                Note(
                    value="Payable within 1 calendar month from the invoice date"
                ),
            ]
        ),
    ],
    allowance_charge=[
        AllowanceCharge(
            charge_indicator=False,
            allowance_charge_reason_code=AllowanceChargeReasonCode(
                value="17"
            ),
            multiplier_factor_numeric=MultiplierFactorNumeric(
                value=Decimal("0.10")
            ),
            amount=Amount(
                value=Decimal("10.00"),
                currency_id="GBP"
            )
        ),
    ],
    tax_total=[
        TaxTotal(
            tax_amount=TaxAmount(
                value=Decimal("17.50"),
                currency_id="GBP"
            ),
            tax_evidence_indicator=True,
            tax_subtotal=[
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal("100.00"),
                        currency_id="GBP"
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal("17.50"),
                        currency_id="GBP"
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value="A"
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="UK VAT"
                            ),
                            tax_type_code=TaxTypeCode(
                                value="VAT"
                            )
                        )
                    )
                ),
            ]
        ),
    ],
    legal_monetary_total=LegalMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal("100.00"),
            currency_id="GBP"
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal("90.00"),
            currency_id="GBP"
        ),
        allowance_total_amount=AllowanceTotalAmount(
            value=Decimal("10.00"),
            currency_id="GBP"
        ),
        payable_amount=PayableAmount(
            value=Decimal("107.50"),
            currency_id="GBP"
        )
    ),
    invoice_line=[
        InvoiceLine(
            id=Id(
                value="A"
            ),
            invoiced_quantity=InvoicedQuantity(
                value=Decimal("100"),
                unit_code="KGM"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("100.00"),
                currency_id="GBP"
            ),
            order_line_reference=[
                OrderLineReference(
                    line_id=LineId(
                        value="1"
                    ),
                    sales_order_line_id=SalesOrderLineId(
                        value="A"
                    ),
                    line_status_code=LineStatusCode(
                        value="NoStatus"
                    ),
                    order_reference=OrderReference(
                        id=Id(
                            value="AEG012345"
                        ),
                        sales_order_id=SalesOrderId(
                            value="CON0095678"
                        ),
                        uuid=Uuid(
                            value="6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1"
                        ),
                        issue_date=XmlDate(2005, 6, 20)
                    )
                ),
            ],
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("17.50"),
                        currency_id="GBP"
                    ),
                    tax_evidence_indicator=True,
                    tax_subtotal=[
                        TaxSubtotal(
                            taxable_amount=TaxableAmount(
                                value=Decimal("100.00"),
                                currency_id="GBP"
                            ),
                            tax_amount=TaxAmount(
                                value=Decimal("17.50"),
                                currency_id="GBP"
                            ),
                            tax_category=TaxCategory(
                                id=Id(
                                    value="A"
                                ),
                                percent=Percent(
                                    value=Decimal("17.5")
                                ),
                                tax_scheme=TaxScheme(
                                    id=Id(
                                        value="UK VAT"
                                    ),
                                    tax_type_code=TaxTypeCode(
                                        value="VAT"
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
                        value="Acme beeswax"
                    ),
                ],
                name=Name(
                    value="beeswax"
                ),
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value="6578489"
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="17589683"
                    )
                ),
                item_instance=[
                    ItemInstance(
                        lot_identification=LotIdentification(
                            lot_number_id=LotNumberId(
                                value="546378239"
                            ),
                            expiry_date=XmlDate(2010, 1, 1)
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("1.00"),
                    currency_id="GBP"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="KGM"
                )
            )
        ),
    ]
)
