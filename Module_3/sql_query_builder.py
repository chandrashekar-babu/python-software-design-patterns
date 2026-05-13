class QueryBuilder:
  def __init__(self):
    self._table = None
    self._columns = ['*']
    self._where = []
    self._order = None
    self._limit = None
 
  def select(self, *columns):
    self._columns = columns
    return self
 
  def from_table(self, table):
    self._table = table
    return self
 
  def where(self, condition):
    self._where.append(condition)
    return self
 
  def order_by(self, column):
    self._order = column
    return self
 
  def limit(self, count):
    self._limit = count
    return self
 
  def build(self):
    query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
    if self._where:
      query += f" WHERE {' AND '.join(self._where)}"
    if self._order:
      query += f" ORDER BY {self._order}"
    if self._limit:
      query += f" LIMIT {self._limit}"
    return query

if __name__ == "__main__":
  query = (QueryBuilder()
    .select('name', 'email')
    .from_table('users')
    .where('age > 18')
    .where('active = true')
    .order_by('name')
    .limit(10)
    .build())
  print(query)  # Output: SELECT name, email FROM users WHERE age > 18 AND active = true ORDER BY name LIMIT 10