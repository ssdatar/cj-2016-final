# Too broad or too harsh: analyzing the California sex offender registry.
Ana Santos and Saurabh Datar

This is a working title

## Elevator pitch
Sex offender laws in California are among the strictest in the nation. The state created a sex registry in 1947 as a tracking tool for law enforcement. Today, the list contains over 100,000 sex offenders, mainly because California requires all offenders, regardless of the type of offense, to register for life. About 80 percent of all the offenders are posted on the Megan's Law website, which we have scraped for this database.

## Inspirations and Prior Work

- [Family Watchdog](http://www.familywatchdog.us/)
  + This is a website that allows people to search for sex offenders in their area by entering their address.
- [Megan's law website](http://www.meganslaw.ca.gov/search.aspx)
  + A website by the CA Department of Justice, this website is another way to search for sex offenders. It even has a nifty map feature that allows search by county. However, the map design and user experience leaves far to be desired.
- [National Sex Offender Public Website](https://www.nsopw.gov/en/)
  + This website is from the SMART office (Office of Sex Offender Sentencing, Monitoring, Apprehending, Registering, and Tracking). This website allows the public to search by first name or last name, zip code or address radius. Each search requires a CAPTCHA entry. It does not allow users to filter by registrant information (i.e. age, race, birthdate or date of conviction). This is a nationwide database.

## Data sources

1. California Sex Offender Registry from the Department of Justice.

## Slimming the data

We have 100,000 rows, which is manageable. Data does not require slimming.

## Joining the data

Joining the data with the county-based reference maps from the [US Census Bureau](https://www.census.gov/geo/maps-data/maps/2010tract.html).

## New categorical variable

- Minors 
	+ Under 18
- Adult (young)
	+ 19 to 40
- Middleage
	+ 41 to 55
- Elderly
	+ 56 and above

## New continuous variable

- Age at time of conviction
- Number of years in the registry
- Summarization
	+ Average of years in the registry, according to categorical variable

## Filtering options

Filter by age category, number of years in the registry, race, location radius, type of crime (offense code), residency status and compliance status

## Views

- Front page: California map with a county/census tract based aggregation of registered sex offender (heat map-type viz)
- Filters: options allowing people to chose what they would like to see
- Results view: showing the list of sex offenders based on user's input along with a filtered map of California

## Visualizations

Map allowing users to visualize filters mentioned above. Some summary charts for offered queries, ex. show me all the offenders who have been convicted for 20 years or more in a bar chart.

## Deployment

Frozen-Flask