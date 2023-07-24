from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BillingReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import CreditNoteLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import DiscrepancyResponse
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoiceDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import ItemInstance
from ubl.models.common.ubl_common_aggregate_components_2_1 import LegalMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import LotIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxCategory
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxSubtotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxTotal
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CreditedQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import LotNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import ReferenceId
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
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
from ubl.models.maindoc.ubl_credit_note_2_1 import CreditNote
from xsdata.models.datatype import XmlDate


obj = CreditNote(
    ublversion_id=UblversionId(
        value="2.0"
    ),
    customization_id=CustomizationId(
        value="urn:oasis:names:specification:ubl:xpath:CreditNote-2.0:sbs-1.0-draft"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-credit-notification-draft"
    ),
    id=Id(
        value="CN758494"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="349ABBAE-DF9D-40B4-849F-94C5FF9D1AF4"
    ),
    issue_date=XmlDate(2005, 6, 25),
    tax_point_date=XmlDate(2005, 6, 21),
    note=[
        Note(
            value="sample"
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
        payable_amount=PayableAmount(
            value=Decimal("107.50"),
            currency_id="GBP"
        )
    ),
    credit_note_line=[
        CreditNoteLine(
            id=Id(
                value="1"
            ),
            note=[
                Note(
                    value="as agreed on phone, the invoice should have been cancelled earlier, apologies"
                ),
            ],
            credited_quantity=CreditedQuantity(
                value=Decimal("100"),
                unit_code="KGM"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("100.00"),
                currency_id="GBP"
            ),
            tax_point_date=XmlDate(2005, 6, 21),
            discrepancy_response=[
                DiscrepancyResponse(
                    reference_id=ReferenceId(
                        value="A00095678"
                    ),
                    description=[
                        Description(
                            value="invoice cancelation"
                        ),
                    ]
                ),
            ],
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
