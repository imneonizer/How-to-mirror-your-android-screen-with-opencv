# How-to-mirror-you-android-screen-with-opencv
This repository contain tools and step by step explanation on "how to mirror your android screen with opencv" and send touch inputs via command line.

Note: This repository contains codes for windows platform only, if you want to use it on linux or Mac OS you need to replace `scrcpy-win64` directory with your suported platform [click here](https://github.com/Genymobile/scrcpy) to download.
>I was always curious to know a way so that i could be able to
>access my android screen so that, i can perform image procssing
>and do some automation tasks like... making Game bots.

### Problems
* I didn't knew any way to stream the android display to my pc.
* Though i found several applications like `apower mirror`, but it was paid application.
* i wanted to interact with the screen itself, but the only way i found was to use my pc's cursor to manually touch the screen from my pc.
* so far i used pyautogui, to automate my pc cursor movements, but the problem was, i wasn't able to interact with my pc while the script ran.
***
### Solution
* Using this useful opensource tool `scrcpy`, which utilises `adb` under the hood to stream android's display directly to my pc.
* since it is using `adb` i can send touch inputs via command line. eg: `adb shell input tap x y`
* The only downside is, `scrcpy` displays the android screen in an separate window, so i need to set the window to `left half` of my pc screen and then using `PIL` to read my pc's screen and there after cropping the Android's screen from the whole pc's screen.
* This idea sounds a little complicated, but it works somehow!
* I am currently working on the `source code` of `scrcpy` so that i could be able to extract the screen as an numpy array directly from my python script, so i don't need to capture my pc's screen and cropping out Android's screen out of it.
** *
## How to Do it YOURSELF!
Step 1:

Open up `Developer options` inside your Android settings and turn on `USB Debugging`

![USB Debugging](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/usb-debugging.png)

Step 2:

Install this app `a paper` from Play Store. we will use this app to test if our script is sending touch inputs to our Android phone.

Step 3:

Ok! Now final time, lets launch our program `capture_android_Screen.py`

![launch](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/launch.png)

Output will be similar to below Image:

![start-up](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/start-up.png)

> Command prompt is showing instructions: `>> Press Enter to continue` , wait till your Android Screen shows up on your pc screen.

After all these steps are completed Arrange your Android screen and Command prompt in the same manner as shown in below image.

![arrange-windows](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/arrange-windows.png)

Now finally you can go to Command prompt and `Hit Enter` to see the magic.
> Before hitting Enter, make sure you have launched the app which we had previously downloaded `a paper`. and pinch in a little bit so that when touch event happens it would show a big black dot on the touched portion of the Android screen.

![launched](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/launch-app.png)

So, if everything goes fine, after `5th Frame`, you will see, a black dot on your Android screen. This means, we were able to register touch to our Android phone via command line.

![result](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/final-show.png)

* if you want to touch at different coordinate on you phone you can pass the coordinate on `line 95`

![code snippet](https://github.com/imneonizer/How-to-mirror-you-android-screen-with-opencv/edit/master/documentation/touch-coordinates.png)

> Vola! I knew you can do it too!

if you face any issues, let me know.. we will figure it out together.
any contributions are most welcom.

Hit me on twitter: @imneonizer

contact: mneonizer@gmail.com

insta: the.nitin.rai
