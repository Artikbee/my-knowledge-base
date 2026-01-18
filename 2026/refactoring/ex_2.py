conn = None


def find_by_user_id(user_id: int):
    """
    Плохо, так как есть уязвимость к SQL-инъекциям
    https://owasp.org/Top10/2025/A05_2025-Injection/
    """
    sql = (
        f"SELECT id,name,role FROM users WHERE user_id='{user_id}'"
    )
    return conn.execute(sql).fetchone()


def find_by_user_id(user_id: int):
    """
    Хорошо, так как используется параметризованный запрос (%s — placeholder)
    """
    sql = (
        "SELECT id,name,role FROM users WHERE user_id= %s"
    )
    params = (user_id,)
    return conn.execute(sql, params).fetchone()
