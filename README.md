## Company Generator, Inc.

This program procedurally generates company names and details. There is a live web version that is generating 100 new companies every five minutes here: https://apps.vickio.net/compgen

Running`main.pl`will print 10 randomly generated companies.

**Requirements:** python>=3.6, `pip install faker`

This project is just for fun. Feel free to contribute. Here are some ideas I have:

### Improvements

* Improve founder name generation (currently just using Faker)
* Make shorter domain names for companies with long names
* Add real city name data instead of the Faker generated cities
* Update fake word generator that `name.pl`uses to have more variety (currently using Faker)

### Additions

* Company history (major events like acquisition, bankruptcy, closing, moving, etc)
* Logo generation
* Company stats (number of employees, offices, revenue, profit, etc)
* Stock ticker and price for public companies
