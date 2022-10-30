import argparse
import csv
import json
import requests

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable):
        return iterable
    tqdm.write = print


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mastodon-url', default='https://mastodon.social', help='Mastodon instance URL, defaults to https://mastodon.social')
    parser.add_argument('--mastodon-token', required=True, help='Mastodon OAuth token, needs `read:accounts` scope')
    parser.add_argument('--twitter-csv', required=True, help='CSV file with twitter accounts data, needs to have a column `username`')
    args = parser.parse_args()

    url_fmt = f'{args.mastodon_url}/api/v1/accounts/search?q={{}}'
    headers = {'Authorization': f'Bearer {args.mastodon_token}'}

    # Get the list of twitter usernames to search in Mastodon
    twitter_usernames = []
    with open(args.twitter_csv) as cf:
        reader = csv.DictReader(cf)
        for row in reader:
            twitter_usernames.append(row['username'])

    for tu in tqdm(twitter_usernames):
        # Get the list of potential matches from Mastodon API
        r = requests.get(url_fmt.format(tu), headers=headers)
        r.raise_for_status()
        mastodon_accounts = r.json()

        # Filter out the empty and suspended ones.
        active_accounts = [acct for acct in mastodon_accounts if not acct.get('suspended')]
        if not active_accounts:
            continue
        tqdm.write(f'Potential accounts for https://twitter.com/{tu}')
        for account in active_accounts:
            acct = account['acct']
            username = account['username']
            display_name = account.get('display_name', None)

            msg = f'* {acct}'
            if display_name and display_name != username:
                msg += f' -- {display_name}'
            msg += f' ({args.mastodon_url}/@{username})'

            tqdm.write(msg)


if __name__ == '__main__':
    main()
