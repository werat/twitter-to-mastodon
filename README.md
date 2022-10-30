# twitter-to-mastodon

Simple Python script to find Twitter users in Mastodon.

## Usage

```bash
❯ python3 twitter-to-mastodon.py -h
usage: twitter-to-mastodon.py [-h] [--mastodon-url MASTODON_URL] --mastodon-token MASTODON_TOKEN --twitter-csv TWITTER_CSV

options:
  -h, --help            show this help message and exit
  --mastodon-url MASTODON_URL
                        Mastodon instance URL, defaults to https://mastodon.social
  --mastodon-token MASTODON_TOKEN
                        Mastodon OAuth token, needs `read:accounts` scope
  --twitter-csv TWITTER_CSV
                        CSV file with twitter accounts data, needs to have a column `username`
```

### Getting Mastodon OAuth token

Go to your Mastodon instance and create a new developer app: `Mastodon -> Account settings -> Development -> New application`. Choose any name and select at least the `read:accounts` OAuth scope. The token you're looking for is `Your access token`.

### Getting Twitter CSV

I didn't want to mess with the Twitter API, so I've exported my following list via <https://www.twtdata.com/>. The first 2000 entries are free, which was more than enough for me.

## Example output

```bash
❯ python3 twitter-to-mastodon.py ...
Potential accounts for https://twitter.com/werat
* werat -- Andy Hippo (https://mastodon.social/@werat)
* weratolts@plume.fedi.quebec (https://mastodon.social/@weratolts)
* weratin@mastodon.host (https://mastodon.social/@weratin)
* Weratepigs@todon.nl (https://mastodon.social/@Weratepigs)
```
