by_sex = """ 
SELECT "PERP_SEX", COUNT(*)
FROM nypd_arrests
GROUP BY "PERP_SEX"
"""

by_boro = """ 
SELECT "ARREST_BORO", COUNT(*)
FROM nypd_arrests
GROUP BY "ARREST_BORO"
"""

by_date = """ 
SELECT "ARREST_DATE", COUNT(*)
FROM nypd_arrests
GROUP BY "ARREST_DATE"
ORDER BY "ARREST_DATE" 
"""

by_race = """ 
SELECT "PERP_RACE", COUNT(*)
FROM nypd_arrests
GROUP BY "PERP_RACE"
"""

by_age = """ 
SELECT "AGE_GROUP", COUNT(*)
FROM nypd_arrests
GROUP BY "AGE_GROUP"
ORDER BY COUNT(*) DESC
"""

by_desc = """ 
SELECT "OFNS_DESC", COUNT(*)
FROM nypd_arrests
GROUP BY "OFNS_DESC"
ORDER BY COUNT(*) DESC
"""


queries = {
    'age': by_age,
    'race': by_race,
    'boro': by_boro,
    'description': by_desc,
    'date': by_date,
    'sex' : by_sex
}