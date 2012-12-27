import requests
import sys


HN_SEARCH_URL = ("http://api.thriftdb.com/api.hnsearch.com/items/_search?q=%s&weights[url]=1.0")
HN_COMMENT_URL = "http://news.ycombinator.com/item?id=%d"


def get_hn_id(url):
    query_url = HN_SEARCH_URL % url
    response = requests.get(query_url)
    body = response.json()
    hits = long(body["hits"])
    if hits > 1:
        sys.stderr.write("Many results, taking first one\n")
    elif hits <= 0:
        sys.stderr.write("No results.\n")
        return None
    result = body["results"][0]["item"]
    return result["id"]


def generate_hn_comments_url(hn_id):
    return HN_COMMENT_URL % hn_id


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <url>" % (__file__)
        sys.exit(1)
    else:
        url = sys.argv[1]

    hn_id = get_hn_id(url)
    if hn_id:
        print generate_hn_comments_url(hn_id)
    else:
        sys.exit(1)
