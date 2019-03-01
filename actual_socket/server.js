const server = require('http').createServer()
const io = require('socket.io')(server)

io.on('connection', function (client) {

  client.on('move', function(direction) {
    console.log('the direction is ', direction)
    io.emit("move", direction)
  })

  client.on('disconnect', function() {
    console.log('the client disconnected')
  })

  client.on('error', function (err) {
    console.log('received error from client:', client.id)
    console.log(err)
  })
})

server.listen(1337, function (err) {
  if (err) throw err
  console.log('listening on port 1337')
})
