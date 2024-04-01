from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BillingReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoiceDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import LegalMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyLegalEntity
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import Person
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RegistrationAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReminderLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import AdditionalStreetName
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentityCode
from ubl.models.common.ubl_common_basic_components_2_1 import Department
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import FamilyName
from ubl.models.common.ubl_common_basic_components_2_1 import FirstName
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import JobTitle
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import MiddleName
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PayableRoundingAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Postbox
from ubl.models.common.ubl_common_basic_components_2_1 import PrepaidAmount
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxInclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_reminder_2_1 import Reminder
from xsdata.models.datatype import XmlDate


obj = Reminder(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    id=Id(
        value='12'
    ),
    issue_date=IssueDate(
        value=XmlDate(2010, 4, 14)
    ),
    accounting_supplier_party=AccountingSupplierParty(
        party=Party(
            endpoint_id=EndpointId(
                value='1234567890123',
                scheme_id='GLN',
                scheme_agency_id='9'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='Supp123',
                        scheme_id='ZZZ'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Salescompany ltd.'
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value='1231412341324',
                    scheme_id='GLN',
                    scheme_agency_id='9'
                ),
                postbox=Postbox(
                    value='5467'
                ),
                street_name=StreetName(
                    value='Main street'
                ),
                additional_street_name=AdditionalStreetName(
                    value='Suite 123'
                ),
                building_number=BuildingNumber(
                    value='1'
                ),
                department=Department(
                    value='Revenue department'
                ),
                city_name=CityName(
                    value='Big city'
                ),
                postal_zone=PostalZone(
                    value='54321'
                ),
                country_subentity_code=CountrySubentityCode(
                    value='RegionA'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='DK',
                        list_id='ISO3166-1',
                        list_agency_id='6'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value='DK12345',
                        scheme_id='DKVAT',
                        scheme_agency_id='ZZZ'
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='VAT',
                            scheme_id='UN/ECE 5153',
                            scheme_agency_id='6'
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value='The Sellercompany Incorporated'
                    ),
                    company_id=CompanyId(
                        value='5402697509',
                        scheme_id='CVR',
                        scheme_agency_id='ZZZ'
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value='Big city'
                        ),
                        country_subentity=CountrySubentity(
                            value='RegionA'
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value='DK'
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value='4621230'
                ),
                telefax=Telefax(
                    value='4621231'
                ),
                electronic_mail=ElectronicMail(
                    value='antonio@salescompany.dk'
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value='Antonio'
                    ),
                    family_name=FamilyName(
                        value='M'
                    ),
                    middle_name=MiddleName(
                        value='Salemacher'
                    ),
                    job_title=JobTitle(
                        value='Sales manager'
                    )
                ),
            ]
        )
    ),
    accounting_customer_party=AccountingCustomerParty(
        party=Party(
            endpoint_id=EndpointId(
                value='1234567987654',
                scheme_id='GLN',
                scheme_agency_id='9'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='345KS5324',
                        scheme_id='ZZZ'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Buyercompany ltd'
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value='1238764941386',
                    scheme_id='GLN',
                    scheme_agency_id='9'
                ),
                postbox=Postbox(
                    value='123'
                ),
                street_name=StreetName(
                    value='Anystreet'
                ),
                additional_street_name=AdditionalStreetName(
                    value='Back door'
                ),
                building_number=BuildingNumber(
                    value='8'
                ),
                department=Department(
                    value='Accounting department'
                ),
                city_name=CityName(
                    value='Anytown'
                ),
                postal_zone=PostalZone(
                    value='101'
                ),
                country_subentity=CountrySubentity(
                    value='RegionB'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='BE',
                        list_id='ISO3166-1',
                        list_agency_id='6'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value='BE54321',
                        scheme_id='BEVAT',
                        scheme_agency_id='ZZZ'
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='VAT',
                            scheme_id='UN/ECE 5153',
                            scheme_agency_id='6'
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value='The buyercompany inc.'
                    ),
                    company_id=CompanyId(
                        value='5645342123',
                        scheme_id='ZZZ',
                        scheme_agency_id='ZZZ'
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value='Mainplace'
                        ),
                        country_subentity=CountrySubentity(
                            value='RegionB'
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value='BE'
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value='5121230'
                ),
                telefax=Telefax(
                    value='5121231'
                ),
                electronic_mail=ElectronicMail(
                    value='john@buyercompany.eu'
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value='John'
                    ),
                    family_name=FamilyName(
                        value='X'
                    ),
                    middle_name=MiddleName(
                        value='Doe'
                    ),
                    job_title=JobTitle(
                        value='Purchasing manager'
                    )
                ),
            ]
        )
    ),
    legal_monetary_total=LegalMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal('1436.5'),
            currency_id='EUR'
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal('1436.5'),
            currency_id='EUR'
        ),
        tax_inclusive_amount=TaxInclusiveAmount(
            value=Decimal('1729'),
            currency_id='EUR'
        ),
        allowance_total_amount=AllowanceTotalAmount(
            value=Decimal('100'),
            currency_id='EUR'
        ),
        charge_total_amount=ChargeTotalAmount(
            value=Decimal('100'),
            currency_id='EUR'
        ),
        prepaid_amount=PrepaidAmount(
            value=Decimal('1000'),
            currency_id='EUR'
        ),
        payable_rounding_amount=PayableRoundingAmount(
            value=Decimal('0.30'),
            currency_id='EUR'
        ),
        payable_amount=PayableAmount(
            value=Decimal('729'),
            currency_id='EUR'
        )
    ),
    reminder_line=[
        ReminderLine(
            id=Id(
                value='1'
            ),
            billing_reference=[
                BillingReference(
                    invoice_document_reference=InvoiceDocumentReference(
                        id=Id(
                            value='TOSL108'
                        )
                    )
                ),
            ]
        ),
    ]
)
