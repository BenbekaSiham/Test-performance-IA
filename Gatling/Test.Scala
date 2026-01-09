import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class Test extends Simulation {

  // Définition de la configuration HTTP
  val httpProtocol = http
    .baseUrl("http://localhost:3000") // URL de base
    .contentTypeHeader("application/json")

  // Définition du scénario
  val scn = scenario("Test POST avec JSON")
    .exec(
      http("Requête POST")
        .post("/api/test")
        .body(StringBody("""{ "message": "Bonjour" }""")).asJson
        .check(status.is(200))
    )

  // Définition de la simulation avec ramp-up de 70 utilisateurs sur 60 secondes
  setUp(
    scn.inject(rampUsers(70).during(60.seconds))
  ).protocols(httpProtocol)
}
