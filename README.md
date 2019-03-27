# Cleanbot
University of Kent student's group project for CO600
# Introduction
The code provided assumes that you have a pre-existing Lego Mindstorms robot that has 2 P-bricks and  7 motors, one for each wheel, another for the claw, one for the arm joint and the last for the arm rotation, to start this does not require you to have a pre existing operating system running on the P-brick's, however 2 Micro SD cards will be needed to be able to install an operating system on the bricks.

We would also recommend installing, if you don't already, Ngrok, this is a way of providing a URL that can tunnel to a specific port on a local machine, something that our project uses extensively.

The overall idea of this project is to create a rover-styled robot that is controlled by Alexa, it can drive around a room and be used with commands to pick up items off the floor, the end-user being potentially people with disabilities.

# 1. Amazon Alexa Services
Working with Alexa involves creating a skill, which can later be delployed to the Alexa store.
To begin with this, you need an Amazon developer account which you can create an account [https://developer.amazon.com/](here). From here go to the Alexa tab, then the 'Alexa skill kit'. You can then create a skill, setting your model as custom. When prompted to choose a template, its best to 'Start from scratch', you've now created a skill.

An intent is a step of functionality for your skill, for our project we have several intents, for movement of the rover, rotating the arm, raising and lowering the arm and for the claw itself. To get all of CleanBot's functionality, you can simply add the intents.json file in the skill folder to the JSON editor tab on Amazon's developer page.

Sample utterances

Adding the endpoint - ngrok
The final step on the Amazon website is registering an endpoint, instead of using a Lambda function our project uses the HTTPS endpoint type. For the URL, you need to run Ngrok, if you haven't done this before here's how, on a mac:
```bash
   cd ~
   ./ngrok http 5000
```
You need to use the https url that is provided and paste it into the default region input, for an SSL certificate, you should select the :
> My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority
You've now set up all of the Alexa side.
# 2. Flask-ask python script
To get communcations from Alexa we used the Flask-ask library that was created for the Alexa skills kit, this allows us to delegate functions to each intent. Further to this we used the SocketIO-Client library to then send commands to the web server.

For our python script to run, you will need to have both the Flask-ask library and the SocketIO-Client libraries installed, so using pip you should install them. The script listens on port 5000 for messages from Alexa, this script is not production ready, this is because an error we found due to the use of Ngrok, where Alexa requests were unable to be verified. 

The final step for this code is to once again, run Ngrok, creating it for port 1337 by running : 
```bash
   cd ~
   ./ngrok http 1337
```
Placing the https URL as the URL inside the SocketIO call in the code. You should then run the script.
# 3. Node.js web socket
The port 1337, is being listened to by our web socket. To begin with the web socket, you need to install Node.js onto your machine. After this, you can simply run : 
```javascript
   npm start
```
The web socket takes messages from the Flask-ask python script and then sends them onto the Ev3 robot, it also sends messages which the test suite can use.
# 4. Ev3dev scripts

Ev3dev - following instructions for flashing sd card
Copying over files to brick
Running the files on the device

# Future advances

# Bash scripts

#Test suite