from gpiozero import Button
from picamera import PiCamera
from time import gmtime, strftime
from overlay_functions import *
from guizero import App, PushButton, Text, Picture, TextBox
from twython import Twython
from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)

def take_picture():
    global output
    output = strftime("/home/pi/Documents/allseeingpi/image-%d-%m %H:%M.png", gmtime())
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)
    output_overlay(output, overlay)

    size = 400, 400
    gif_img = Image.open(output)
    gif_img.thumbnail(size, Image.ANTIALIAS)
    gif_img.save(latest_photo, 'gif')

    your_pic.set(latest_photo)

def new_picture():
    camera.start_preview(alpha=128)
    preview_overlay(camera, overlay)

def send_tweet():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    name = name_box.get()
    twitterhandle = twitterhandle_box.get()
    emailaddress = emailaddress_box.get()
    postcode = postcode_box.get()

    #Creating one variable storing all the information input
    concatenated = name + ", " + twitterhandle + ", " + emailaddress + ", " + postcode

    #apending latest input to the data file ready for analysis at later point
    fh = open("data.csv","a")
    fh.write(concatenated)
    fh.write("\n")
    fh.close() 
    
    message = twitterhandle + " Hi there! Here's some more information about Code Club www.codeclub.org.uk"
    with open(output, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)

    name_box.clear()
    twitterhandle_box.clear()
    emailaddress_box.clear()
    postcode_box.clear()

next_overlay_btn = Button(23)
next_overlay_btn.when_pressed = next_overlay

take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

camera = PiCamera()
camera.resolution = (800, 480)
camera.hflip = True

output = ""

latest_photo = '/home/pi/Documents/allseeingpi/latest.gif'

app = App("The All-Seeing Pi", 800, 600)
##app.attributes("-fullscreen", True)
message = Text(app, "Nice to meet you!")
your_pic = Picture(app, latest_photo)
new_pic = PushButton(app, new_picture, text="New picture")

name_label = Text(app, "What's your Name? ")
name_box = TextBox(app, "", width=30)

twitterhandle_label = Text(app, "What's your Twitter handle? ")
twitterhandle_box = TextBox(app, "", width=30)

emailaddress_label = Text(app, "What's your Email address? ")
emailaddress_box = TextBox(app, "", width=30)

postcode_label = Text(app, "What's your Postcode? ")
postcode_box = TextBox(app, "", width=30)

tweet_pic = PushButton(app, send_tweet, text="Tweet picture")
app.display()
