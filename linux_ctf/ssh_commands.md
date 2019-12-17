## SOURCES
[Traversly Media](https://www.youtube.com/watch?v=hQWRp-FdTpc)
[Traversly gist](https://gist.github.com/bradtraversy/f03df587f2323b50beb4250520089a9e)


## What is SSH
- Can be used with SFTP


## Creating public/private key pairs
- Running the `ssh-keygen` will create two keys one private and one public
```
# Private key
~/.ssh/id_rsa

# Public, the one that goes on the server
~/.ssh/id_rsa.pub
```
- You will put the public key in the `authorized_keys` folder
```
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
```