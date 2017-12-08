# Python-project
This program performs parsing of the OLX trading platform for "iphone-X".

The basic URL components are written in the program, and they search in the category of mobile devices.
Requests for relevant URLs receive page data and are processed.
All of the functions and objects used belong to the standard Python 3.6 objects and objects.
To write the code, the text editor "Notepad ++" and the compiler from the official site "python.org" were used.
The graphical interface contains 14 objects "label", 1 object "Text" and two objects "Button".


 -  def get_html (url): - get a page
 - def get_last_page (html): - Selects the serial number of the last page
 - def write_csv (data): - write to file
 - def get_page_data (html): - select the information on the announcements on the current page
 - def main (console): - the main function which is called when the buttons are pressed and uses all of the above functions for obtaining data
