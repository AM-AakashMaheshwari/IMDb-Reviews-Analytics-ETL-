def upsert_table_sql(table, key_cols):
    # Template using MERGE (simplified, must customize per table)
    key_cond = ' AND '.join([f"target.{col} = source.{col}" for col in key_cols])
    sql = f"""
    MERGE INTO {table} AS target
    USING (SELECT ? AS {', ? AS '.join(key_cols)}) AS source
    ON ({key_cond})
    WHEN MATCHED THEN
        UPDATE SET ... -- define columns
    WHEN NOT MATCHED THEN
        INSERT (...) VALUES (...); -- define insert columns
    """
    return sql