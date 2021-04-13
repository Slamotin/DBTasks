# -*- coding: utf-8 -*-
#Получить все фильмы заданного режиссера
#Получить всех людей, которые работали вместе с заданным человеком
#Посчитать число актеров в каждом фильме
import neo4j

def run_request(session, body):
    result = session.run(body)
    return [record for record in result]

uri = "bolt://localhost:7687"
driver = neo4j.GraphDatabase.driver(uri, auth=("neo4j","12345"), max_connection_lifetime=1000)
session = driver.session()

director_name = "\'Robert Zemeckis\'"
people_name = "\'Robert Zemeckis\'"

request1 = run_request(session, 
"MATCH (p:Person {name:" + people_name 
+ "}) - [:DIRECTED] - (m:Movie) RETURN m.title")

request2 = run_request(session,
"MATCH (people: Person {name:" + people_name 
+ "}) - [] - (:Movie) <- [relatedTo] - (work_with: Person) RETURN work_with.name")

request3 = run_request(session, 
"MATCH (m:Movie)-[:ACTED_IN]-(people:Person) RETURN m.title, count(people)")



session.close()
driver.close()


