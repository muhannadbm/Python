"""
Module determining pilot certifications, ratings, and endorsements.

The restrictions that we place on a pilot depend on their qualifications.  There are three
ways to think about a pilot.  

(1) Certifications.  These are what licenses a pilot has.  We also use these to classify
where the student is in the licensing process.  Is the student post solo (can fly without
instructor), but before license?  Is the student 50 hours past their license (a threshold 
that helps with insurance)?

(2) Ratings.  These are extra add-ons that a pilot can add to a license. For this project,
the only rating is Instrument Rating, which allows a pilot to fly through adverse weather
using only instruments.

(3) Endorsements. These are permission to fly certain types of planes solo.  Advanced 
allows a pilot to fly a plane with retractable landing gear. Multiengine allows a pilot
to fly a plane with more than one engine.

The file pilots.csv is a list of all pilots in the school, together with the dates that
they earned these certifications, ratings, and endorsements.  Specifically, this CSV file
has the following header:
    
    ID  LASTNAME  FIRSTNAME  JOINED  SOLO  LICENSE  50 HOURS  INSTRUMENT  ADVANCED  MULTIENGINE

The first three columns are strings, while all other columns are dates.

The functions in this class take a row from the pilot table and determine if a pilot has
a certain qualification at the time of takeoff. As this program is auditing the school 
over a course of a year, a student may not be instrument rated for one flight but might
be for another.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Muhannad Bani Almarje
Date: 03/16/2021
"""
import utils
import datetime


# CERTIFICATION CLASSIFICATIONS
# The certification of this pilot is unknown
PILOT_INVALID = -1
# A pilot that has joined the school, but has not soloed
PILOT_NOVICE  = 0
# A pilot that has soloed but does not have a license
PILOT_STUDENT = 1
# A pilot that has a license, but has under 50 hours post license
PILOT_CERTIFIED = 2
# A pilot that 50 hours post license
PILOT_50_HOURS  = 3

# ID,LAST NAME,FIRST NAME,JOINED,SOLO,LICENSE,50 HOURS,INSTRUMENT,ADVANCED,MULTIENGINE
def get_certification(takeoff,student):
    """
    Returns the certification classification for this student at the time of takeoff.
    
    The certification is represented by an int, and must be the value PILOT_NOVICE, 
    PILOT_STUDENT, PILOT_CERTIFIED, PILOT_50_HOURS, or PILOT_INVALID. It is PILOT_50_HOURS 
    if the student has certified '50 Hours' before this flight takeoff.  It is 
    PILOT_CERTIFIED if the student has a private license before this takeoff and 
    PILOT_STUDENT is the student has soloed before this takeoff.  A pilot that has only
    just joined the school is PILOT_NOVICE.  If the flight takes place before the student
    has even joined the school, the result is PILOT_INVALID.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
                        # Implement this function
    i=3
    length = len(student)
    tempstudent = student
    while i < length:
        if type(student[i]) != datetime.datetime:
            tempstudent[i] = utils.str_to_time(student[i],takeoff.tzinfo)
        i = i + 1

    if student[6] != None:
        if tempstudent[6] <= takeoff:

            return PILOT_50_HOURS
    if student[5] != None:
        if tempstudent[5] <= takeoff:

            return PILOT_CERTIFIED
    if student[4] != None:
        if tempstudent[4] <= takeoff:

            return PILOT_STUDENT
    if student[3] != None:
        if tempstudent[3] <= takeoff:

            return PILOT_NOVICE

    return PILOT_INVALID


def has_instrument_rating(takeoff,student):
    """
    Returns True if the student has an instrument rating at the time of takeoff, False otherwise
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    NOTE: Just because a pilot has an instrument rating does not mean that every flight
    with that pilot is an IFR flight.  It just means the pilot could choose to use VFR
    or IFR rules.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
                       # Implement this function   
    result = utils.str_to_time(student[7],takeoff.tzinfo)
    if result != None:
        return result < takeoff
    else:
        return False


def has_advanced_endorsement(takeoff,student):
    """
    Returns True if the student has an endorsement to fly an advanced plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
                       # Implement this function
    result = utils.str_to_time(student[8])
    if result != None:
        return result < takeoff
    else:
        return False


def has_multiengine_endorsement(takeoff,student):
    """
    Returns True if the student has an endorsement to fly an multiengine plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
                        # Implement this function
    result = utils.str_to_time(student[9])
    if result != None:
        return result < takeoff
    else:
        return False


def get_minimums(cert, area, instructed, vfr, daytime,minimums):
    """
    Returns the most advantageous minimums for the given flight category.
    
    The minimums is the 2-dimensional list (table) of minimums, including the header.
    The header for this table is as follows:
        
        CATEGORY  CONDITIONS  AREA  TIME  CEILING  VISIBILITY  WIND  CROSSWIND
    
    The values in the first four columns are strings, while the values in the last
    four columns are numbers.  CEILING is a measurement in ft, while VISIBILITY is in
    miles.  Both WIND and CROSSWIND are speeds in knots.
    
    This function first searches the table for rows that match the function parameters. 
    It is possible for more than one row to be a match.  A row is a match if ALL four 
    of the first four columns match.
    
    The first column (CATEGORY) has values 'Student', 'Certified', '50 Hours', or 'Dual'.
    If the value 'Student', it is a match if category is PILOT_STUDENT or higher.  If
    the value is 'Certified, it is a match if category is PILOT_CERTIFIED or higher. If
    it is '50 Hours', it is only a match if category is PILOT_50_HOURS. The value 'Dual' 
    only matches if instructed is True.
    
    The second column (CONDITIONS) has values 'VMC' and 'IMC'. A flight filed as VFR 
    (visual flight rules) is subject to VMC (visual meteorological conditions) minimums.  
    Similarly, a fight filed as IFR is subject to IMC minimums.
    
    The third column (AREA) has values 'Pattern', 'Practice Area', 'Local', 
    'Cross Country', or 'Any'. Flights that are in the pattern or practice area match
    'Local' as well.  All flights match 'Any'.
    
    The fourth column (TIME) has values 'Day' or 'Night'. The value 'Day' is only 
    a match if daytime is True. If it is False, 'Night' is the only match.
    
    Once the function finds the all matching rows, it searches for the most advantageous
    values for CEILING, VISIBILITY, WIND, and CROSSWIND. Lower values of CEILING and
    VISIBILITY are better.  Higher values for WIND and CROSSWIND are better.  It then
    returns this four values as a list of four floats (in the same order they appear)
    in the table.
    
    Example: Suppose minimums is the table
    (cert, area, instructed, vfr, daytime, minimums
        
        CATEGORY   CONDITIONS  AREA           TIME  CEILING  VISIBILITY  WIND  CROSSWIND
        Student    VMC         Pattern        Day   2000     5           20    8
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Certified  VMC         Practice Area  Night 3000     10          20    10
        50 Hours   VMC         Local          Day   3000     10          20    10
        Dual       VMC         Any            Day   2000     10          30    10
        Dual       IMC         Any            Day   500      0.75        30    20
    
    The call get_minimums(PILOT_CERTIFIED,'Practice Area',True,True,True,minimums) matches
    all of the following rows:
        
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Dual       VMC         Any            Day   2000     10          30    10
    
    The answer in this case is [2000,5,30,20]. 2000 and 5 are the least CEILING and 
    VISIBILITY values while 30 and 20 are the largest wind values.
    
    If there are no rows that match the parameters (e.g. a novice pilot with no 
    instructor), this function returns None.
    
    Parameter cert: The pilot certification
    Precondition: cert is in int and one PILOT_NOVICE, PILOT_STUDENT, PILOT_CERTIFIED, 
    PILOT_50_HOURS, or PILOT_INVALID.
    
    Parameter area: The flight area for this flight plan
    Precondition: area is a string and one of 'Pattern', 'Practice Area' or 'Cross Country'
    
    Parameter instructed: Whether an instructor is present
    Precondition: instructed is a boolean
    
    Parameter vfr: Whether the pilot has filed this as an VFR flight
    Precondition: vfr is a boolean
    
    Parameter daytime: Whether this flight is during the day
    Precondition: daytime is boolean
    
    Parameter minimums: The table of allowed minimums
    Precondition: minimums is a 2d-list (table) as described above, including header
    """
    # Find all rows that can apply to this student
    # Find the best values for each column of the row
    row=len(minimums)
    col=len(minimums[0])
    categorylist=[]
    conditionlist=[]
    arealist=['Any',str(area)]
    daylist=[]
    result=[]
    
    if cert == -1:
        categorylist = []
        
    if cert >= PILOT_STUDENT:
        categorylist.append('Student')
        
    if cert >= PILOT_CERTIFIED:
        categorylist.append('Certified')
        
    if cert >= PILOT_50_HOURS:
        categorylist.append('50 Hours')
    
    
    if area == 'Pattern' or area == 'Practice Area':
        arealist.append('Local')
        arealist.append(str(area))
    elif area == 'Any':
        arealist.append('Pattern')
        arealist.append('Local')
        arealist.append('Practice Area')
        arealist.append('Cross Country')
    
    if instructed == True:
        categorylist.append('Dual')
        
    if vfr == True:
        conditionlist.append('VMC')
    else:
        conditionlist.append('IMC')
        
    if daytime == True:
        daylist.append('Day')
    else:
        daylist.append('Night')


    for r in range(row):
        x = minimums[r]
        if x[0] in categorylist and x[1] in conditionlist and x[2] in arealist and x[3] in daylist:
            result.append(minimums[r])

    if len(result) == 0:
        return None

    resultrow=len(result)
    mincieling = float(result[0][4])
    minvisibility = float(result[0][5])
    maxwind=0
    maxcrosswind=0

    for r in range(resultrow):
        if float(result[r][4]) < mincieling:
            mincieling = float(result[r][4])
            
        
        if float(result[r][5]) < minvisibility:
            minvisibility = float(result[r][5])
        
        if float(result[r][6]) > maxwind:
            maxwind = float(result[r][6])

        if float(result[r][7]) > maxcrosswind:
            maxcrosswind = float(result[r][7])
            
    result = [float(mincieling),float(minvisibility),float(maxwind),float(maxcrosswind)]

    return result
                
                
