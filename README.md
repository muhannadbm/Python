# Description
A number of projects, sorted by complexity from lowest to highest, programmed in Python, these projects include processing input images, and handling large amount of complex data and process it and coming with an output according to that data, Projects are explained in details below:
 
# Modules
- Coding-an-interactive-script: (A simple die roller)
  - die.py: A simple die roller

- **Programming-with-functions: (Some operations on strings)
  - funcs.py: 
    - matching_parens(String s) function: Returns True if the string s has a matching pair of parentheses.
    - first_in_parens(String s) function: Returns The substring of s that is inside the first pair of parentheses.

- **Challange-problems: (Some operations on strings)
  - exercise1/funcs.py: A function to find all instances of a substring.
  
  - exercise2/funcs.py: Returns the text encoded by shifting each letter by n positions. (Caesar-style substitution ciphers).
  
  - exercise2/funcs.py: a Module for scoring blackjack hands.
  
- **Implementing-a-currency-converter: (A project that use a webservice to obtain results according to criteria defined by the user and return it to him)
  - currency.py: (Module for currency exchange)
    - before_space(String s): Returns the substring of s up to, but not including, the first space.
    - after_space(String s): Returns the substring of s after the first space
    - first_inside_quotes(String s): Returns the first substring of s between two (double) quote characters
    - get_src(String json): Returns the src value in the response to a currency query.
    - get_dst(String json): Returns the dst value in the response to a currency query.
    - has_error(String json): Returns True if the response to a currency query encountered an error.
    - service_response(String src,String dst, Int amt) function: Returns a JSON string that is a response to a currency query.
    - iscurrency(String currency): Returns True if currency is a valid (3 letter code for a) currency.
    - exchange(String src,String dst, Int amt): Returns the amount of currency received in the given exchange.
  - exchangeit.py: (User interface for module currency)



- **Processing-images: (a Project consisting of various image processing functions)
  - plugins.py: 
    - mono(image, sepia=False): Returns True after converting the image to monochrome.
    - flip(image,vertical=False): Returns True after reflecting the image horizontally or vertically.
    - transpose(image): Returns True after transposing the image.
    - rotate(image,right=False): Returns True after rotating the image left of right by 90 degrees.
    - vignette(image): Returns True after vignetting (corner darkening) the current image.
    - blur(image,radius=5): Returns True after bluring the image.


- **Auditing-datasets:(a Project to analyze data(json and cvs) from airlines company's flights and pilots information and weather reports during those flights and list all violations with details of each violation or write them to a file)**
  - auditor/utils.py: (Module providing utility functions for this project.)
    - read_csv(filename): Returns the contents read from the CSV file filename.
    - write_csv(data,filename): Writes the given data out as a CSV file filename.
    - read_json(filename): Returns the contents read from the JSON file filename.
    - str_to_time(timestamp,tz=None): Returns the datetime object for the given timestamp (or None if stamp is invalid)
    - daytime(time,daycycle): Returns true if the time takes place during the day.
    - get_for_id(id,table): Returns (a copy of) a row of the table with the given id.
              
  - auditor/pilots.py: (Module determining pilot certifications, ratings, and endorsements.)
    - get_certification(takeoff,student): Returns the certification classification for this student at the time of takeoff.
    - has_instrument_rating(takeoff,student): Returns True if the student has an instrument rating at the time of takeoff, False otherwise
    - has_advanced_endorsement(takeoff,student): Returns True if the student has an endorsement to fly an advanced plane at the time of takeoff.
    - has_multiengine_endorsement(takeoff,student): Returns True if the student has an endorsement to fly a multiengine plane at the time of takeoff.
    - get_minimums(cert, area, instructed, vfr, daytime,minimums): Returns the most advantageous minimums for the given flight category.
              
  - auditor/violations.py: (Module to check violations for a flight lesson.)
     - bad_visibility(visibility,minimum): Returns True if the visibility measurement violates the minimum, False otherwise
     - bad_winds(winds,maxwind,maxcross): Returns True if the wind measurement violates the maximums, False otherwise
     - bad_ceiling(ceiling,minimum): Returns True if the ceiling measurement violates the minimum, False otherwise
     - get_weather_report(takeoff,weather): Returns the most recent weather report at or before take-off.
     - get_weather_violation(weather,minimums): Returns a string representing the type of weather violation (empty string if flight is ok)
     - list_weather_violations(directory): Returns the (annotated) list of flight reservations that violate weather minimums.
              
  - auditor/app.py: (Module that validates the flight school's records.)
     - discover_violations(directory,output): Searches the dataset directory for any flight lessons the violation regulations.
     - execute(args): Executes the application or prints an error message if executed incorrectly.
