from database.DB_connect import DBConnect
from model.hotspot import Location


class DAO():
    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct nwhl.Provider 
                    from nyc_wifi_hotspot_locations nwhl 
                    order by nwhl.Provider asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Provider"])

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getNodes(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct n.Location
                    from nyc_wifi_hotspot_locations n
                    where n.Provider = %s"""

        cursor.execute(query, (provider,))

        for row in cursor:
            result.append(row["Location"])

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getEdges(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select nwhl.Location as n1Loc, nwhl2.Location as n2Loc, avg(nwhl.Latitude) as n1Lat, avg(nwhl.Longitude) as n1Long, avg(nwhl2.Latitude) as n2Lat, avg(nwhl2.Longitude) as n2Long  
                    from nyc_wifi_hotspot_locations nwhl, nyc_wifi_hotspot_locations nwhl2 
                    where nwhl2.Provider = nwhl.Provider and nwhl2.Provider  = %s 
                    and nwhl.OBJECTID < nwhl2.OBJECTID 
                    and nwhl2.Location <> nwhl.Location
                    group by nwhl2.Location, nwhl.Location"""

        cursor.execute(query, (provider,))

        for row in cursor:
            loc1 = Location(row["n1Loc"], row["n1Lat"], row["n1Long"])
            loc2 = Location(row["n2Loc"], row["n2Lat"], row["n2Long"])
            result.append((loc1, loc2))

        cursor.close()
        conn.close()

        return result



