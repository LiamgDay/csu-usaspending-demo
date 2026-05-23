import pandas as pd
from usaspending import USASpendingClient

from campuses import CSU_CAMPUSES
from fetch_grants import fetch_awards_for_recipient
from transform_grants import award_to_row
from summarize_grants import summarize_awards, format_dollars


all_rows = []

with USASpendingClient() as client:

    for campus in CSU_CAMPUSES:

        campus_name = campus["display_name"]

        for approved_recipient_name in campus["approved_recipient_names"]:

            print(f"\nFetching awards for: {approved_recipient_name}")
            print("campus | agency | award_type | amount | start_date | end_date")

            awards = fetch_awards_for_recipient(
                client,
                approved_recipient_name
            )

            for award in awards:

                row = award_to_row(
                    award,
                    campus_name,
                    approved_recipient_name
                )

                all_rows.append(row)

                print(
                    f"{row['campus']} | "
                    f"{row['agency']} | "
                    f"{row['award_type']} | "
                    f"{format_dollars(row['amount'])} | "  
                    f"{row['start_date']} | "
                    f"{row['end_date']}"
                )


print(f"\nTotal rows collected: {len(all_rows)}")

summarize_awards(all_rows)


"""df = pd.DataFrame(all_rows)

df.to_csv(
    "output/csu_awards_demo.csv",
    index=False
)

print("\nCSV saved to output/csu_awards_demo.csv")"""