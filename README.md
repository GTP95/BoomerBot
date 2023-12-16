# BoomerBot
An IRC bot to make fun of a certain other IRC bot. Based on [pydle](https://github.com/shizmob/pydle), so requires Python 3.6 through 3.9.  
Supports NickServ authentication, no SASL yet as it isn't supported by the Azzurra IRC network.
Usage: `python main.py [-h] [-s SERVER] [-p PASSWORD] nickname realname listOfChannels [listOfChannels ...]`  
```
positional arguments:
  nickname              nickname to use
  realname              realname to use
  listOfChannels        list of channels to join

optional arguments:
  -h, --help            show help message and exit
  -s SERVER, --server SERVER
                        server to connect to
  -p PASSWORD, --password PASSWORD
                        password to use for NickServ authentication
```
Defaults to connecting to `raccooncity.azzurra.org` without NickServ authentication.

## Run locally
To run it locally, first install the dependencies with `pip install -r requirements.txt`  
Then run it with `python main.py <nick> <realname> <list_of_space_separated_channels>`

## Docker
To run it inside a docker container, first build the image with `docker build -t boomerbot .`  
Then run it with `docker run -d --restart unless-stopped boomerbot boomerbot <nick> <realname> <list_of_space_separated_channels>`
If you're using Bash, remember to escape the `#` in the channel list with `\#`.