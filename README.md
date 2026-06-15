# CSU USAspending Demo
A demo project that pulls grant data for three CSU campuses from the USAspending API using the Planetary Society's ORM, with plans to expand to all CSU campuses and eventually serve as the backend for a dashboard application.

## Purpose
The long-term goal of this project is to make publicly available federal grant data for CSU campuses easier to explore and analyze through a lightweight dashboard interface.

Additionally, this project is intended to demonstrate the general workflow behind interacting with the USAspending API using the Planetary Society's ORM. The structure of this demo is meant to eventually extend to all CSU campuses as the foundation for a dashboard that enables easier interaction with USAspending grant data.

Currently, the demo compiles grant information for San Luis Obispo, San Diego, and Channel Islands, including awarded grants and summary statistics on top awarding agencies and largest awards. The project is also intended to demonstrate the basic capabilities and workflow of working with the Planetary Society's ORM.

## Walkthrough
The few campuses included are outlined in campuses.py where I tie their reference name (like "San Luis Obispo") to their various aliases that appear in the USAspending API database (like "California Polytechnic State University" or often misspelled entries such as "San Diego State University Fou"). The fetch_grants.py file uses this list to determine what kind of API requests to send in, heavily relying on TPS' ORM. The pulled information is then converted into rows using transform_grants.py. Then, summary data is constructed with summarize_grants.py. The main.py file puts all of this together and prints the outputs in a somewhat readable way. 

## Notes
- At the bottom of main.py is commented out code that would save a copy of the tables printed as a .csv to the /output folder if one wanted to do this. This is mainly here for future plans where whichever dashboard tool I use will most likely want a .csv version of this information to interact with.
- For demonstration purposes, main.py only pulls up to 5 awards for each of the various names related to each CSU. I have set it to default to just 5 grants so as to not add unnecessary work to the API just for the demo. This default can be changed by adding a parameter to the fetch_awards_for_recipient call in lines 23 to 26.
```python
awards = fetch_awards_for_recipient(
    client,
    approved_recipient_name
)
```
currently defaults to a limit of 5, but can be changed to 
```python
awards = fetch_awards_for_recipient(
    client,
    approved_recipient_name,
    limit=None
)
```
or 
```python
awards = fetch_awards_for_recipient(
    client,
    approved_recipient_name,
    limit=100
)
```

- It'd be great to also display an abbreviation like "NASA" but the ORM's .abbreviation strangely returns the agency code just like .code does. We can later hard code a dictionary of codes with their abbreviations so we can run something like .code.to_abbreviation where to_abbreviation would take the code and convert it to the correct abbreviation.

## Setup
Requires Python 3.11+.

Clone the repository:

```bash
git clone https://github.com/LiamgDay/csu-usaspending-demo.git
cd csu-usaspending-demo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

This project uses the Planetary Society's `usaspending-ORM` package to query and work with USAspending.gov award data.

This project was developed with the assitance of Claude.
