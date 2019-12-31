## Python asyncfpg 
[**Source Docs**](https://magicstack.github.io/asyncpg/current/index.html)

> Connection pools allow you to create a pool of connections that can be shared this lowers
the amount of resources needed and it proven to be up to 6 times faster than manually establishing
connections when needed to interact with the database.
```python
# Establish a pool of connections
import asyncio, asyncpg
loop = asyncio.get_event_loop()
postgres = "dsn string"
pool = await loop.run_until_complete(asyncpg.create_pool(postgres, command_timeout=60))
```
> The pool of connections is just that, a pool. To interact with the database you must fist request
for a connection from the pool. This is done by using the `acquire()` method. With a connection
acquired, you can then run your tasks. When complete you return the connection back to the pool
by using a `release()`. What is confusing is that `release()` is a method of the `pool` object so 
when you invoke it you have to pass the connections as an argument.
```python
# Request connection and release
con = await pool.acquire()
await pool.release(con)
```
### Acquiring connections
> As mentioned above, you must request a connection from the pool in order to communicate with the
database and then release the connection. You can do this in two ways. Manually as shown above and
using the `with` context manager.

#### `1` Manually
```python
con = await pool.acquire()
try:
    await con.execute(...)
finally:
    await pool.release(con)
```
### `2` Context with
```python
async with pool.acquire() as con:
    await con.execute(...)
```
### Closing connections
> This one can be as simple as issuing a `await pool.close()` but there can be a time when
you are stuck waiting for some tasks to finish this is why it is advised to use the 
`coroutine asyncio.wait_for()` this will cause a an error to raise which instructs the pool to send
a `Pool.terminate()` to the connection. This prevents you from waiting for ever and still gracefully
with force to close the connection
```python
# Wait a max of 3 seconds before sending terminate()
try:
    await asyncio.wait_for(pool.close(), timeout=3.0)
except asyncio.TimeoutError:
    print("Automatically sent a terminate()")
```
### Other methods
```python
# Request a connection
con = await pool.acquire()

# Perform sql
await con.execute(sql)
await con.executre('''
    INSERT INTO table (a) VALUES (100), (200), (300);''')
await con.execute('''
    INSERT INTO table (a) VALUES ($1), ($2)
    ''', 10, 20)

# Perform sql on each item in a container
await con.execut('''
    INSERT INTO table (a) VALUES ($1, $2, $3);
    ''', [(1, 2, 3), (4, 5, 6)])

# Retrieve information
await con.fetch(sql) # all records
await con.fetchrow(sql) # First record
await con.fetchval(sql, 0) # First record, nth index

# Release connection
await pool.release(con, timeout=seconds.float)

# Return all open connections back to the pool
await con.expire_connections()
```

### Record objects
> Record objects (those that return from a fetch) have very neat characteristics. They can be accessed
via their index or their column name.
```python
record = "fetch_object"
record[0] == record['first_column']
```
> You can even cast the record object into a `dict` or `tuple`
```python
record = "fetch_object"
record_dict = dict(record)
record_tuple = tuple(record)
```
 

## Docker-composed used
```dockerfile
version: '3.7'
services:
  frosch_postgres:
    container_name: frosch_postgres
    image: postgres:12.1-alpine
    restart: always
    networks:
      - zulu_network
    environment:
      POSTGRES_USER: pgadmin4life
      POSTGRES_PASSWORD: ${PASSWORD}
      POSTGRES_DB: pantherdb
      POSTGRES_PORT: 5432
      PGDATA: /var/lib/postgresql/data
    volumes:
      - frosh_db:/var/lib/postgresql/data
    ports:
      - 5432:5432
```


## Setting up PostGresSQL Docker

| Command | Description |
| ------- | -------- |
| `docker pull postgres` | Pulls the postgres socker image to your machine |
| `docker pull postgres:<tag>` | Can specify a version tag to pull others like older versions or smaller versions like the alphine one |
| `docker images` | You should be able to see your new image that you downloaded |
| `docker run --name <nickname> --link <nickname>:<nickname> -e POSTGRES_PASSWORD=<passwd> -d postgres:<tag>` | Run the image that you downloaded by giving it an alias, an evironment variable and run it detached to get the terminal back just like & does with apps |
| `-p <port>:<5423>` | Specify the port that the OS should listen on to pass to the container, this is added befofore the image name *postgres* |
| `docker ps` | Show that the container is running |
| `docker exec -it <image from ps> bash` | Get an interactive shell with the image using bash |
| `psql -U postgres` | Get a admin shell to the DB |

## PostGresSQL Commands

| Command | Description |
| ------- | -------- |
| `psql -U postgres` | Get a db shell with the user, by default postgres is the admin user |
| `\du` | Display users with their roles |
| `create database <name>;` | Create a database under the context of the user you are logged on with |
| `\l` | List available databases |
| `\c <db>` | Connect to a DB |
| `\d` | List relations in the connected DB |
| `\d+ <table>` | Get more information on a table |
| `\q` | Quit out of the current db session |
| `\dt` | Show the tables in the current db you are connected to |


## Connecting to the Docker DB externally
```bash
psql -h 127.0.0.1 -p <port> -U <user> -d <database>
```

### Random coc notes for testing
```
pip install git+https://github.com/mathsman5133/coc.py --upgrade
client = coc.login(<email>, <passwd>)
# Malforn fix
coc.utils.correct_tag
player = await client.get_player('#9P9PRYQJ')
```