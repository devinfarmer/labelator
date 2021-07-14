# Labelator, but better
The MCCS Okinawa Library program uses this to create labels using the call numbers scraped from the OPAC.
The idea is to have a simple, easy way to format call number labels with the appropriate size font and number of spaces for readability and consistency.
Staff only need to scan the Item ID on a computer (ideally a headless Raspberry Pi) with a Zebra label printer, this script will gather the call number from the OPAC, format the text, and print a label.
