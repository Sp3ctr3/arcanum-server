import argparse
from werkzeug.serving import make_ssl_devcert
parser = argparse.ArgumentParser(description='Generate SSL cert')
parser.add_argument('host', type=str,
                   help='host to be used in SSL cert')
args = parser.parse_args()
path=make_ssl_devcert('key', args.host)
print "Keys written to ", path
