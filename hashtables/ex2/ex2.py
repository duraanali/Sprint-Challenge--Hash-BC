#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        print("ticket top", ticket)

    key = "NONE"

    for i in range(length):
        current_ticket = hash_table_retrieve(hashtable, key)
        print("current_ticket", i, current_ticket)
        route[i] = current_ticket
        key = current_ticket
      
        

    return route[:-1]

# tickets = [Ticket("PIT", "ORD"),Ticket("XNA", "SAP"), Ticket("SFO", "BHM"),Ticket("FLG", "XNA"),Ticket("NONE", "LAX"),Ticket("LAX", "SFO"),Ticket("SAP", "SLC"), Ticket("ORD", "NONE"), Ticket("SLC", "PIT"), Ticket("BHM", "FLG")]

# print(reconstruct_trip(tickets, 10))