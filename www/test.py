import orm
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop,user='test',password='password',db='awesome')
    u = User(name='Test',email='Test@example.com',passwd='123456',image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
