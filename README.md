# BoomerBot
An IRC bot to make fun of a certain other IRC bot. Based on [pydle](https://github.com/shizmob/pydle), so requires Python 3.6 through 3.9.  
Usage: `python main.py <nick> <realname> <list_of_space_separated_channels>`  
Note: automatically connects to the Azzurra network, there's no option to specify a server other than editing the code yet.

## Run locally
To run it locally, first install the dependencies with `pip install -r requirements.txt`  
Then run it with `python main.py <nick> <realname> <list_of_space_separated_channels>`

## Docker
To run it inside a docker container, first build the image with `docker build -t boomerbot .`  
Then run it with `docker run -d docker run -d --restart unless-stopped boomerbot boomerbot <nick> <realname> <list_of_space_separated_channels>`
If you're using Bash, remember to escape the `#` in the channel list with `\#` or put the whole list in quotes.