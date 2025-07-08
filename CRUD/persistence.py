from db import get_connection


class CountryRepository:
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
    def add(self, datos_pais):
        Code, Name, Population, Capital, Poblacion_Capital = datos_pais
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("SELECT ID FROM city WHERE Name = %s AND Population = %s LIMIT 1", (Capital, Poblacion_Capital))
        city = cursor.fetchone()
        if city:
            capital_id = city[0]
        else:
            cursor.execute("INSERT INTO city (Name, Population, Code) VALUES (%s, %s, %s)", (Capital, Poblacion_Capital, Code))
            capital_id = cursor.lastrowid
        
        cursor.execute(
            "INSERT INTO country (Code, Name, Population, Capital) VALUES (%s, %s, %s, %s)",
            (Code, Name, Population, Capital)
        )
        conn.commit()
        cursor.close()
        conn.close()
    
    def update(self, Code, Name, Population, Capital, Poblacion_Capital):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE country SET Name = %s, Population = %s, Capital = %s, Poblacion_Capital = %s WHERE Code = %s",
            (Name, Population, Capital, Poblacion_Capital, Code)
        )
        conn.commit()
        cursor.close()
        conn.close()
