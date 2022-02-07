from twisted.internet import reactor, endpoints
from website import web_site

if __name__ == "__main__":
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
    endpoint.listen(web_site)
    reactor.run()
