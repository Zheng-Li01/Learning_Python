import time, json, os,asyncio, logging
from aiohttp import web
from datetime import datetime
logging.basicConfig(level=logging.INFO)

# def index(request):
#     return web.Response(body=b'<h1>hello</h1>', content_type='text/html')

# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)

#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9090)
#     logging.info('server started at http://127.0.0.1:9090...')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    return web.Response(body=b'<h1>Awesome App</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:9257...')
    web.run_app(app, host='127.0.0.1', port=9527)


init()