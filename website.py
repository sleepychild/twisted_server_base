from twisted.web.server import Site
from twisted.web.resource import Resource

index_html: str = """
<html>
<head>
<title>Python Twisted</title>
</head>
<body>
<h1>Demo Site</h1>
<p>This is just for testing purposes</p>
</body>
</html>
"""


class Index(Resource):
    isLeaf = True
    session = set()

    def render_GET(self, request):
        return index_html.encode()


site_index: Index = Index()
web_site: Site = Site(site_index)
