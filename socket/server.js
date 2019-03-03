//Import packages
// Import packages
const express = require("express");
const socketIO = require("socket.io");
const path = require("path");

// Configuration
const PORT = process.env.PORT || 1337;
const INDEX = path.join(__dirname, 'test.html');

// Start server
const server = express()
  .use((req, res) => res.sendFile(INDEX) )
 .listen(PORT, () => console.log("Listening on localhost:" + PORT));

// Initiatlize SocketIO
const io = socketIO(server);

io.on('connection', function (client) {

  client.on('move', function(direction) {
    console.log('the direction is ', direction);
    io.emit("move", direction);
    io.emit('message','move',direction);
  })

  client.on('claw',function(action) {
    if(action == 'grab') {
      console.log('Claw is grabbing');
    } else {
      console.log('Claw is releasing');
    }
    io.emit('claw',action);
    io.emit('message','claw',action);
  })

  client.on('arm',function(direction) {
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
    io.emit('arm',direction);
    io.emit('message','arm',direction);
  })

  client.on('disconnect', function() {
    console.log('the client disconnected')
  })

  client.on('error', function (err) {
    console.log('received error from client:', client.id)
    console.log(err)
  })
})

// server.listen(1337, function (err) {
//   if (err) throw err
//   console.log('listening on port 1337')
// })
