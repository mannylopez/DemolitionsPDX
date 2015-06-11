### Display Home Demolition Permits of Portland

## Goal:

[The Portland Chronicle](http://www.portlandchronicle.com/) blog does a great job covering land use and development news for the city of Portland, OR.

They update a [Demolition map](http://www.portlandchronicle.com/demolition-permit-map/) and a list of permits that are issued by the city of Portland on a weekly basis.

I tried to reverse engineer this:

* The [Bureau of Development Services](https://www.portlandoregon.gov/bds/) publishes [Metro Reports](https://www.portlandoregon.gov/bds/41449) in PDF format on a weekly basis that lists all building permit applications, issued building permits, and land use review intakes.

* Either a script or a person goes through the [Metro Report](https://www.portlandoregon.gov/bds/41449) and creates a list of all of the Demolition permits that were issued during that week. This is hard to do since the Demolition form is not standardized. Examples include "DEMOLISH SINGLE FAMILY RESIDENCE", "DEMOLISH SFR", "DEMOLISH ONE SINGLE FAMILY RESIDENCE WITH BASEMENT", And "DEMO SFR" to include a few examples.

* Note that the city of Portland also requires demolitions permits for garages and other structures, but for this project, we are only looking for home demolition permits.

* Either a script or a person adds the new permits to the [demolition permit map](http://www.portlandchronicle.com/demolition-permit-map/).

As a fun exercise, I wanted to create an automatic process for this workflow.


## Sources
* [Data Journalism Hanbook](http://datajournalismhandbook.org/1.0/en/getting_data_3.html)

* [The Hitchhiker’s Guide to Python! HTML Scraping](http://docs.python-guide.org/en/latest/scenarios/scrape/)

*

## To DO


## Workflow
1. Scrape demolition data from [The Portland Chronicle](http://www.portlandchronicle.com/)

2. Save Address and Permit Issued fields as CSV

3. Conver CSV to GeoJSON using [Mapbox Omnivore](https://github.com/mapbox/leaflet-omnivore)

4. Add point to a leaflet map


- Ran into unicode problems when trying to write the address data to CSV because it could not write

http://www.joelonsoftware.com/articles/Unicode.html
https://docs.python.org/2/howto/unicode.html

The scraping script breaks, or returns a unicode value when it encounters a link. In this case, it is the u'\xa0' code which represents a ['non-breaking space'](http://en.wikipedia.org/wiki/Non-breaking_space).


I created a test
```code
if u'\xa0' in mayTwentyFiveBlock:
  print "FIX ME"
```
to flag events where this happens.

and included a line that replaces those instances within the array with the coordinates for [Null Island](https://github.com/nixta/null-island)
