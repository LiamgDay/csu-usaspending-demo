from typing import Any


def award_to_row(award: Any, campus_name: str, approved_recipient_name: str) -> dict[str, Any]:
    """
    Convert one USAspending award object into a clean dictionary row.
    """
    return {
        "campus": campus_name or "Unknown campus",
        "approved_recipient_name": approved_recipient_name,
        "actual_recipient_name": award.recipient.name or "Unknown recipient",
        "recipient_uei": award.recipient.uei or "Unknown UEI",
        "recipient_id": award.recipient.recipient_id or "Unknown recipient ID",
        "award_id": award.award_identifier or "Unknown award ID",
        "award_type": award.type_description or "Unknown type",
        "agency": award.awarding_agency.name or "Unknown agency",
        #"agency_abbreviation": award.awarding_agency.abbreviation or "Unknown agency abbreviation",
        "agency_code": award.awarding_agency.code or "Unknown agency code",
        "amount": award.total_obligation, # Decimal
        "start_date": award.start_date, # datetime.date
        "end_date": award.end_date, # datetime.date
        "description": award.description or "Unknown description",
        "usa_spending_url": award.usa_spending_url or "Unknown usa spending URL",
    }