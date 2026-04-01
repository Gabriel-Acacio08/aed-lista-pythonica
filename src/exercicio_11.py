def modify_guest_list(guests: list[str], unavailable: str, new_guest: str) -> list[str]:
    index = guests.index(unavailable)
    guests[index] = new_guest
    return guests
