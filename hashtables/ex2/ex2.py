#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #set empty dictionary and list
    flight = {}
    route = []
    
    """
    * loop through the param length
    * key set to ticket's starting point
    * value set to ticket's next airport along the way
    * set flight to current stop with key/value
    """
    for i in range(length): 
        key = tickets[i].source
        value = tickets[i].destination
        flight[key] = value    
    
    """
    * key "None" = start of flight
    * key/value "None" = end of flight
    * add stops to the route until key/value is "None"
    """
    
    #start of flight
    key = flight["NONE"]
    
    #add stops to the route
    while key !="NONE":
        route.append(key)
        #set next stop in flight
        key = flight[key]
        
    #Add final stop so key/value is "None"
    route.append(key)

    return route
