Meteorite Landings Analysis

A Python script that analyzes NASA's Meteorite Landings dataset (~45,700 records) and produces summary statistics plus a 4-panel visualization covering mass, fall type, meteorite class, and geographic distribution.

What it does

data_analysis.py:


Loads meteorite-landings.csv and drops rows missing year, mass, reclat, or reclong, keeping only records with year <= 2026.
Prints summary stats to the console:

Mean and median mass (grams)
Fell vs. Found counts and percentage fallen
Top 5 most common meteorite classes (recclass)



Generates a 2x2 chart grid saved to meteorite_charts.png:

Fell vs Found bar chart
Top 5 Meteorite Classes bar chart
Geographic Distribution scatter plot (longitude vs. latitude)
Feature Correlation heatmap (mass, year, reclat, reclong)





Setup

bashpip install -r requirements.txt

Requires Python 3.8+ with pandas, matplotlib, and seaborn.

Usage

Place meteorite-landings.csv in the same directory as the script, then run:

bashpython data_analysis.py

Output: console report + meteorite_charts.png.

Data

meteorite-landings.csv — one row per meteorite, with columns:

ColumnDescriptionnameMeteorite nameidUnique identifiernametypeValid or relictrecclassMeteorite classification (e.g., L6, H5, EH4)massMass in gramsfallFell (observed falling) or Found (discovered after the fact)yearYear of fall or findreclat / reclongLatitude / longitude of the recovery locationGeoLocationCombined lat/long string

A note on the printed "insights"

The script's console output includes interpretive claims (e.g., that near-zero correlations "prove" impacts are "completely random," or that desert/Antarctic clustering is purely a visibility effect). These read more like narrative flourishes than statistically supported conclusions — a near-zero Pearson correlation only rules out a linear relationship, and the geographic clustering is also strongly driven by where organized recovery expeditions have searched (e.g., systematic Antarctic and Saharan meteorite surveys), not just visibility against terrain. Worth keeping in mind if this report is shared further.
