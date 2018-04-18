const fastify = require('fastify')()
const pino = require('pino')()

const MONGO_CONNEXION_ISSUE = 2

function failFast(msg, code) {
  pino.error(msg)
  process.exit(code)
}

if (!process.env.MONGO_PASSWD) failFast("Missing env MONGO_PASSWD", MONGO_CONNEXION_ISSUE)

const mongoURL = `mongodb+srv://auto_garden:${process.env.MONGO_PASSWD}@davdtests-x5mnt.mongodb.net/test`

pino.info(`Mongo URL: ${mongoURL}`)

fastify.register(require('fastify-mongodb'), {
  url: mongoURL
})

fastify.get('/', function (request, reply) {
  reply.send({ hello: 'world' })
})

fastify.post('/log', function (request, reply) {

  const payload = request.body

  pino.info('Going to store log.')
  pino.info(payload)

  const db = this.mongo.db
  db.collection('logs', (err, col) => {
    if (err) {
      pino.error(err)
      return reply.send(err)
    }

    col.insert(payload, (err, result) => {
      reply.send(result)
    })
  })
})

// RUN SERVER
fastify.listen(process.env.WEBSVC_PORT || 3000, '0.0.0.0', function (err) {
  if (err) throw err
  pino.info(`server listening on ${fastify.server.address().port}`)
})