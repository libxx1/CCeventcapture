# CCeventcapture
An 'All-seeing Pi' and Staff Picademy 'Mug Shot' mashup 

All files are to be stored in the directory /home/pi/Documents/allseeingpi/ and subdirectory /overlays per structure here. 

This project is for use at Code Club events as a way of showing off the Raspberry Pi, having something interactive for on the PiTop Ceed, sending useful information to people who visit the stand and collecting data for post event analysis. 

You'll need 4 m2f wires, a breadboard, 2 buttons and a camera. Setup details (including python library installs) are in the fab resource https://www.raspberrypi.org/learning/the-all-seeing-pi/ stick to the same GPIO pins as thats how allseeingpievent.py is set up. The file IMG_0691.jpg shows how to set it up though for events forget the proto board and connect straight to the Raspberry Pi so that setup is more visible to people.

If you change the overlays you'll need to update the file names list in overlay_functions.py . You'll also need to change the text in the twitter message within allseeingpievent.py to make it relevant for your event. Lastly you'll need to change the keys in auth.py so they are those for your twitter account. 

Once you're happy with your set up you can uncomment the full screen line in allseeingpievent.py 

Give me a shout if you want to chat about everything and of course if you can enhance this project or make the code more efficient then fill ya boots :) 

Cheers, Liz
