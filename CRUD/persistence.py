from db import get_connection


class CustomerRepository:
    def fetch_all(self):
        query = """
        SELECT 
            country.Code, 
            country.Name, 
            country.Population, 
            city.Name AS Capital, 
            city.Population AS Poblacion_Capital
        FROM 
            country
        JOIN 
            City ON country.Capital = city.ID;
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def delete(self, Code):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM country WHERE Code = %s", (Code))
        conn.commit()
        cursor.close()
        conn.close()

    # métodos add(id), update(id), etc.
