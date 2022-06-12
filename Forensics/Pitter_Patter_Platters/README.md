<p align="center"><img src="../../images/Pitter_Patter_Platters0.png" ></p>

In this challenge, we are provided with disk image to analyze. Hint suggests that we can do it both without mounting that image and with image mounted. Decided to try analyzing it both ways. Firstly, without mounting the image, we can use 'strings' tool to check the contents. Getting satisfying results requires a little bit of tinkering however. After playing with different options for a while, I found out that specifying 16-bit little endian format seems to be the most elegant way:

<p align="center"><img src="../../images/Pitter_Patter_Platters1.png" ></p>

We could technically also grep for pico, but we would need to know beforehand that the string is reversed. To retrieve the correctly formatted flag, we can use 'rev' tool:

<p align="center"><img src="../../images/Pitter_Patter_Platters2.png" ></p>

If we want to solve the challenge by mounting the image however, there are some handy forensics tools that we can use as well. The most popular ones seem to be FTK Imager and Autopsy. Decided to try Autopsy as it was preinstalled in my Kali version. To invoke it, we can simply type 'sudo autopsy', open our browser and navigate to localhost at port 9999:

<p align="center"><img src="../../images/Pitter_Patter_Platters3.png" ></p>

One thing is that, Autopsy prefers if we disable javascript for security reason. To do it in Firefox we can simply navigate to about:config and search for javascript.enabled, then change it to false (remember to enable it again after using Autopsy, otherwise most websites won't work):

<p align="center"><img src="../../images/Pitter_Patter_Platters4.png" ></p>
<p align="center"><img src="../../images/Pitter_Patter_Platters5.png" ></p>

