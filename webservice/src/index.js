const fastify = require('fastify')()

const MONGO_CONNEXION_ISSUE = 2

function failFast(msg, code) {
  console.error(msg)
  process.exit(code)
}

if (!process.env.MONGO_PASSWD) failFast("Missing env MONGO_PASSWD", MONGO_CONNEXION_ISSUE)

const mongoURL = `mongodb://auto_garden:${process.env.MONGO_PASSWD}@davdtests-shard-00-00-x5mnt.mongodb.net:27017,davdtests-shard-00-01-x5mnt.mongodb.net:27017,davdtests-shard-00-02-x5mnt.mongodb.net:27017/test?ssl=true&replicaSet=davdTests-shard-0&authSource=admin`

console.log(`Mongo URL: ${mongoURL}`)

fastify.register(require('fastify-mongodb'), {
  url: mongoURL
})

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