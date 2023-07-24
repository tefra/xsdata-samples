from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BillingReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitution
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitutionBranch
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoiceDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoicePeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PayeeFinancialAccount
from ubl.models.common.ubl_common_aggregate_components_2_1 import PayeeParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import PaymentMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RemittanceAdviceLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import AccountTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import BalanceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CreditLineAmount
from ubl.models.common.ubl_common_basic_components_2_1 import CurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import DebitLineAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PaymentMeansCode
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplierAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalCreditAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TotalDebitAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TotalPaymentAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_remittance_advice_2_1 import RemittanceAdvice
from xsdata.models.datatype import XmlDate


obj = RemittanceAdvice(
    ublversion_id=UblversionId(
        value="2.0"
    ),
    customization_id=CustomizationId(
        value="urn:oasis:names:specification:ubl:xpath:RemittanceAdvice-2.0:sbs-1.0-draft"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-remittance-advice-notification-draft"
    ),
    id=Id(
        value="6577884"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="84E081CE-F9D1-94C5-40F9-94C5FF9D1AC3"
    ),
    issue_date=XmlDate(2005, 6, 22),
    note=[
        Note(
            value="dummy as sample"
        ),
    ],
    total_debit_amount=TotalDebitAmount(
        value=Decimal("107.50"),
        currency_id="GBP"
    ),
    total_credit_amount=TotalCreditAmount(
        value=Decimal("0.00"),
        currency_id="GBP"
    ),
    total_payment_amount=TotalPaymentAmount(
        value=Decimal("107.50"),
        currency_id="GBP"
    ),
    invoice_period=[
        InvoicePeriod(
            start_date=XmlDate(2005, 6, 1),
            end_date=XmlDate(2005, 7, 1)
        ),
    ],
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
    payee_party=PayeeParty(
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
    ),
    payment_means=PaymentMeans(
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
    remittance_advice_line=[
        RemittanceAdviceLine(
            id=Id(
                value="1"
            ),
            note=[
                Note(
                    value="please note that local offices will close for recess for the next three weeks - please send their invoices to central offices for that time"
                ),
            ],
            debit_line_amount=DebitLineAmount(
                value=Decimal("107.50"),
                currency_id="GBP"
            ),
            credit_line_amount=CreditLineAmount(
                value=Decimal("0.00"),
                currency_id="GBP"
            ),
            balance_amount=BalanceAmount(
                value=Decimal("107.50"),
                currency_id="GBP"
            ),
            originator_customer_party=OriginatorCustomerParty(
                party=Party(
                    party_name=[
                        PartyName(
                            name=Name(
                                value="The Terminus"
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
                            value="S Massiah"
                        ),
                        telephone=Telephone(
                            value="0127 98876545"
                        ),
                        telefax=Telefax(
                            value="0127 98876546"
                        ),
                        electronic_mail=ElectronicMail(
                            value="smassiah@the-email.co.uk"
                        )
                    )
                )
            ),
            billing_reference=[
                BillingReference(
                    invoice_document_reference=InvoiceDocumentReference(
                        id=Id(
                            value="A00095678"
                        ),
                        uuid=Uuid(
                            value="849FBBCE-E081-40B4-906C-94C5FF9D1AC3"
                        ),
                        issue_date=XmlDate(2005, 6, 21)
                    )
                ),
            ]
        ),
    ]
)
