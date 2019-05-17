// This web socket is used to transmit request from the Python script to the Ev3Dev scripts
// This web socket listens on the port 1337

// Import packages
const express = require("express");
const socketIO = require("socket.io");
const path = require("path");

// Configuration
const PORT = process.env.PORT || 1337;
const INDEX = path.join(__dirname, 'test.html');

// Start server
const server = express()
// Sets a page to display
  .use((req, res) => res.sendFile(INDEX) )
 .listen(PORT, () => console.log("Listening on localhost:" + PORT));

// Initiatlize SocketIO
const io = socketIO(server);

io.on('connection', function (client) {
  // Prints for testing when a connection made
  console.log("Connection made");
  // Run when a moveIntent is made
  client.on('move', function(direction) {
    // Prints for testing
    console.log('the direction is ', direction);
    // emits the command for the ev3
    io.emit("move", direction);
    // emits the command for the test suite
    io.emit('message','Move message' + " " + direction);
  })

  // Run when the grabIntent or releaseIntent is made
  client.on('claw',function(action) {
    // Prints for testing based on the action
    if(action == 'grab') {
      console.log('Claw is grabbing');
    } else {
      console.log('Claw is releasing');
    }
    // emits the command for the ev3
    io.emit('claw',action);
    // emits the command for the test suite
    io.emit('message','Claw message ' + " "  + action);
  })

  // When a turnArmIntent is made
  client.on('arm',function(direction) {
    // Prints based on testing, collectively based on vertical/horizontal direction
    if(direction == 'up' || direction == 'down') {
      if(direction == 'up') {
        console.log('Arm is going up');
      } else {
        console.log('Arm is going down');
      }
    } else {
      if(direction == 'left') {
        console.log('Arm is moving left');
      } else {
        console.log('Arm is moving right');
      }
    }
    // emits the command for the ev3
    io.emit('arm',direction);
    // emits the command for the test suite
    io.emit('message','arm' + " " + direction);
  })

  // When a disconnect happens
  client.on('disconnect', function() {
    // Prints for testing
    console.log('the client disconnected')
  })

  // When an error occurs
  client.on('error', function (err) {
    // Prints for testing
    console.log('received error from client:', client.id)
    console.log(err)
  })
})

// server.listen(1337, function (err) {
//   if (err) throw err
//   console.log('listening on port 1337')
// })
