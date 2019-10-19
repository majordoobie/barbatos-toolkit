
# Setting up PostGresSQL Docker

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
psql -h 127.0.0.1 -p <port> -U postgres
# Promts for password
localhost:8080/api/v1/<db>
```

## Live Experimental
- Downloaded and established a interactive terminal
```
docker pull postgres


docker run -d --expose 127.0.0.1:5423:5432/tcp --name=pg_db \
    -e POSTGRES_PASSWD=fucker postgres

docker exec -it 6936af5eef80 bash
```
- I did a PS of the container itself and I can see the creds in the enviromental `FUCKING YIKES`
- Running the psql gave me access without cred prompting. I am assuming that it is because it matched the creds of the box? Well I supposed the creds were passed in the environment so maybe it used that? `magic`
```
psql -U postgres
```

# Potential Schema
```
user_registration(
    coc_tag             :   player.tag                      :str
    coc_name            :   player.name                     :str

    coc_clan_name       :   player.clan.name                :str
    coc_clan_tag        :   player.clan.tag                 :str
    coc_clan_share_link :   player.clan.share_link          :str

    coc_badge_url       :   player.league.badge.small       :str
    coc_townhall_level  :   player.town_hall                :int
    coc_trophies        :   player.trophies                 :int
    coc_best_trophies   :   player.best_trophies            :int
    coc_share_link      :   player.share_link               :str
    coc_role            :   player.role                     :str
    
)
```
```
user_update (
    coc_war_stars       :   player.coc_war_stars            :int
    coc_attack_wins     :   player.attack_wins              :int
    coc_defense_wins    :   player.defense_wins             :int
)
```
## coc.py
```
pip install git+https://github.com/mathsman5133/coc.py --upgrade
```
### Establish a client object
```
client = coc.login(<email>, <passwd>)
```
### Malform tags
```
coc.utils.correct_tag
```
### Rando
```
player = await client.get_player('#9P9PRYQJ')
```