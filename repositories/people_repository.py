from datasources.mysql_datasource import mysqlDataSource

class PeopleRepository:

    def listPeople(self, offset, limit):
        totalQuery = ("SELECT count(*) FROM people.people")
        pagQuery = ("SELECT name, surname, email FROM people.people LIMIT %s,%s")

        cursor = mysqlDataSource.getCursor()

        cursor.execute(totalQuery)
        result = {
            'total': cursor.fetchone()[0]
        }

        cursor.execute(pagQuery, (offset, limit))
        result['data'] = cursor.fetchall()

        mysqlDataSource.closeConnection()

        return result


peopleRepository = PeopleRepository()