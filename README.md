campuses.py:          stores the 3 campus search terms

fetch_grants.py:      talks to USAspending

transform_grants.py:  converts ORM objects into clean rows

main.py:              runs the demo

output/:              stores generated CSV files

## Future Plans
### Various Naming Schemes

- Campuses are referred to by many names. Ex: CSU Fresno shows up as "California State University, Fresno" or "California State University Fresno", notice the lack of a comma. 
- Sometimes, one variant of a campus name confusingly shows up twice as distinct "recipients" in USASpending.gov. Ex: "California State University Fresno" shows up twice. In this specific example though, one of those appearances is only tied to one grant out of all 228 grants sent to the identical names. This seems to be due to the Recipient UEI not being provided, or the Recipient Location being very short (Fresno, CA, 93726 as opposed to 4910 N. Chestnut Ave, Fresno, CA, 93726 seen in many other grants).
- I need to figure out which  recipient names I care about, and in the case that we care about many distinct names, I need to attribute all information from all the various names to one entity "CSU Fresno". 

### Types of Awards

-Some money sent to universities comes from the government, but isn't a grant. I found some COVID relief loans. Not sure if these are desirable to view, or if they should be excluded. As of right now, I will exclude them. To include, just research through the various names for each CSU on usaspending.gov and allow awards from types other than grants.

### Agency Abbreviation

-It'd be great to also display an abbreviation like "NASA" but the orm's .abbreviation strangely returns the agency code just like .code does. 
-We can later hard code a dictionary of codes with their abbreviations so we can run something like .code.to_abbreviation where to_abbreviation would take the code and convert it to the correct abbreviation.

### .csv

-Dashboard tools like streamlit and Power BI like to use data in the form of a .csv. There is capability to save the outputs as a .csv in the main file, it is currently commented out at the bottom of the file. By simply uncommenting it, it will save .csv's of only the api pulls (not the summarized data at this point) to the output folder.

This project uses the Planetary Society's `usaspending-orm` package to query and work with USAspending.gov award data.