# RaspberryPi-DHT22-Ubidots
This project uses a Raspberry Pi connected to a DHT22 sensor to read the temperature and humidity of its surroundings to a website called Ubidots, this site then plots these readings as charts and allows real-time analytics to be performed.
## Components
<ol>
  <li> Raspberry Pi B+ [or later]</li>
  <li> Gobbler </li>
  <li> Breadboard </li>
  <li> Connecting wires </li>
  <li> DHT22 [or DHT11] Digital Humidity and Temperature Sensor </li>
  <li> Power Source for Raspberry Pi </li>
  <li> An ethernet cable or a Wifi Module [USB ones work fine] </li>
</ol>

## Requirements
<ul>
  <li> Router with DHCP capability</li>
  <li> Wired or wireless Router </li>
</ul>

## Circuit Diagram
Download Fritzing from <a href="http://fritzing.org/download/">here</a> and open the <a href="https://github.com/KaushikNeelichetty/RaspberryPi-DHT22-Ubidots/blob/master/Ubidots-DHT22-Pi-Connections.fzz">Fritzing project</a> to have a better idea about the connections.<br>

<img src="https://github.com/KaushikNeelichetty/RaspberryPi-DHT22-Ubidots/raw/master/Ubidots-DHT22-Pi-Connections_bb.png"/>

## Pre Connection Procedure
<ol>
  <li> Flash the <a href="https://www.raspberrypi.org/downloads/raspbian/">Raspbian Jessie OS</a> into the MicroSD card of your Raspberry Pi using the <a href="https://sourceforge.net/projects/win32diskimager/">Win32 Disk Imager</a> Software</li>
  <li> Insert the MicrSD card into your Rapsberry Pi </li>
  <li> Download and run <a href="http://www.putty.org/"> Putty</a>, a SSH Client.
  <li> Power up the Raspberry Pi and connect it to your router using an ethernet cable</li>
  <li> Determine the IP Address of your Raspberry pi from the router and enter that IP Address as hostname in the Hostname text field in putty</li>
  <li> Connect to the Pi using putty, even if the connection refuses once or twice, its okay, try again, it will connect. </li>
  <li> The default username is "pi" and password is "raspberry", login to your pi using these credentials </li>
  <li> Expand the file system  in Raspberry pi <code>sudo raspi-config</code> </li>
  <li> Set the time zone of the system in Raspberry pi <code>sudo raspi-config</code></li>
  <li> Run the udpate a few times <code>sudo apt-get update</code> </li>
  <li> Install the necessary softwares <code>sudo apt-get install git-core python-dev python-pip python-smbus</code> .These will come in handy later </li>
  <li> Then reboot, <code>sudo reboot</code> </li>
</ol>

## Preparing the Pi for DHT22 / DHT11
<ol>
  <li> Connect the sensor to the Pi as shown in the circuit diagram </li>
  <li> <code>git clone https://github.com/adafruit/Adafruit_Python_DHT.git</code> to clone the ADafruit DHT repository into your Pi</li>
  <li> <code>cd Adafruit_Python_DHT</code> </li>
  <li> <code>sudo apt-get install build-essential python-dev python-openssl</code> to install the necessary packages needed to install external python libraries</li>
  <li> <code>sudo python setup.py install</code> to install the external library</li>
  <li><code>cd examples</code></li>
  <li> <code>sudo ./AdafruitDHT.py 2302 4</code> to run the example and check if the sensor is working or not</li>
</ol>

## Installing Ubidots package
<p>This is a simple three step procedure, just run the following commands<br>
<code>sudo apt-get install python-setuptools</code><br>
<code>sudo easy_install pip</code><br>
<code>sudo pip install ubidots</code><br>
</p>

## The Python Script
<ol> 
  <li>Sign up at <a href="https://app.ubidots.com/accounts/signup/">Ubidots</a></li>
  <li>Go to Sources and create a new source</li>
  <li>Click on the source you just created</li>
  <li>Add two variables, one called Humidity and other called Temperature, honestly you can create as many variables as you want and call them whatever you want, but for this project what we need are these two.</li>
  <li>In the right bottom of the screen, select the Device wizard and select Raspberry Pi, then give the units for each variable, the number of seconds you want the delay between each reading to be and hit generate code.</li>
  <li>The code needed to send the data to the Ubidots source is generated, copy it and create a python script.</li>
  <li>This script sends random data and it is not the actual data we want to send, now we need to use the Adafruit Python DHT library and create the rest of the script needed. 
    <br>Add these lines of code in the appropriate places<br>
    <code>import sys</code><br>
          <code>import Adafruit_DHT</code><br>
          <code>#Set the type of sensor and the pin for sensor</code><br>
          <code>sensor = Adafruit_DHT.DHT22</code><br>
          <code>pin = 4</code><br>
    <br>
    Within the try block inside the While(1): add this line<br>
    <code>humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)</code><br>
    And replace the variables value1 with humidity and value2 with temperature<br>
    Remove the lines that assign values to value1 and value2.
  </li>
  <li>Run the code using <code> sudo python fileName.py </code> </li>
  <li>Check the values in the variable, they keep updating as and when the Pi sends the value</li>
  <li>You can create widgets with the values, download the data, or send that data as a public link.</li>
</ol>

## Snapshots
The data when viewed in the Data Soruce<br>
<img src="https://github.com/KaushikNeelichetty/RaspberryPi-DHT22-Ubidots/raw/master/VariableView.png"><br>
The data when viewed as widgets<br>
<img src="https://github.com/KaushikNeelichetty/RaspberryPi-DHT22-Ubidots/raw/master/DashboardView.png"><br>
