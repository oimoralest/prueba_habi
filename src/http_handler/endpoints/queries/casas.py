class GetCasas:
    QUERY = """
        SELECT p.id, p.address, p.city, p.year, s.name, p.price, p.description
        FROM (
                SELECT
                    property_id,
                    MAX(update_date) AS update_date
                FROM status_history
                GROUP BY
                    property_id
            ) as temp
            JOIN property p ON temp.property_id = p.id
            JOIN status_history sh ON sh.property_id = temp.property_id
            AND sh.update_date = temp.update_date
            JOIN status s ON sh.status_id = s.id
    """
