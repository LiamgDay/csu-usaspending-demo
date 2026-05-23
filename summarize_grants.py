from collections import defaultdict
from typing import Any
from decimal import Decimal


def format_dollars(amount: Decimal | None) -> str:
    if amount is None:
        return "Unknown amount"

    return f"${amount:,.2f}"


def summarize_awards(rows: list[dict[str, Any]]) -> None:
    """
    Print basic summary statistics for transformed USAspending award rows.
    """

    if not rows:
        print("\nNo awards found to summarize.")
        return

    total_awards = len(rows)
    total_amount = sum((row.get("amount") or 0) for row in rows)

    totals_by_campus = defaultdict(Decimal)
    counts_by_campus = defaultdict(int)

    totals_by_agency = defaultdict(Decimal)
    counts_by_agency = defaultdict(int)

    for row in rows:
        campus = row.get("campus") or "Unknown campus"
        agency = row.get("agency") or "Unknown agency"
        amount = (row.get("amount") or 0)

        totals_by_campus[campus] += amount
        counts_by_campus[campus] += 1

        totals_by_agency[agency] += amount
        counts_by_agency[agency] += 1

    print("\n=== CSU Grants Summary ===")
    print(f"Total awards: {total_awards}")
    print(f"Total funding: {format_dollars(total_amount)}")

    print("\n--- By Campus ---")
    for campus, amount in sorted(
        totals_by_campus.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(
            f"{campus}: "
            f"{counts_by_campus[campus]} awards, "
            f"{format_dollars(amount)}"
        )

    print("\n--- Top 3 Agencies by Funding ---")
    for agency, amount in sorted(
        totals_by_agency.items(),
        key=lambda item: item[1],
        reverse=True
    )[:3]:
        print(
            f"{agency}: "
            f"{counts_by_agency[agency]} awards, "
            f"{format_dollars(amount)}"
        )

    print("\n--- Top 3 Awards by Amount ---")
    print("amount | campus | agency | recipient name | award ID")
    top_awards = sorted(
        rows,
        key=lambda row: row.get("amount") or 0,
        reverse=True
    )[:3]

    for row in top_awards:
        amount = row.get("amount") or 0
        campus = row.get("campus") or "Unknown campus"
        agency = row.get("agency") or "Unknown agency"
        recipient = row.get("actual_recipient_name") or "Unknown recipient"
        award_id = row.get("award_id") or "Unknown award ID"

        print(
            f"{format_dollars(amount)} | "
            f"{campus} | "
            f"{agency} | "
            f"{recipient} | "
            f"{award_id}"
        )