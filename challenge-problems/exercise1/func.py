"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Muhannad Bani Almarje
Date: 2/1/2021
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    tup=()
    i=0
    pos=0
    while i <len(text):
        pos=introcs.find_str(text,sub,i)
        if pos ==-1:
            tup=tup
            
        else:
            if pos in tup:
                tup=tup
            else:
                tup=tup+(pos,)
            
        i=i+1
        
    return tup