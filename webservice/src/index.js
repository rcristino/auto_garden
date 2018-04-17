const fastify = require('fastify')()

fastify.register(require('fastify-mongodb'), {
  url: 'mongodb://localhost:27017/auto_garden_webapp'
})

const MONGO_CONNEXION_ISSUE = 0

function failFast(msg, code) {
  console.error(msg)
  process.exit(code)
}

fastify.get('/', function (request, reply) {
  reply.send({ hello: 'world' })
})

fastify.post('/log', function (request, reply) {
  console.log(request.payload)

  const db = this.mongo.db
  db.collection('logs', (err, col) => {
    if (err) return reply.send(err)

    col.insert(request.payload.data, (err, result) => {
      reply.send(result)
    })
  })
})

// RUN SERVER
fastify.listen(process.env.WEBSVC_PORT || 3000, '0.0.0.0', function (err) {
  if (err) throw err
  console.log(`server listening on ${fastify.server.address().port}`)
})