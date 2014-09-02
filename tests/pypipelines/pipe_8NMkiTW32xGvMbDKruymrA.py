# Pipe pipe_8NMkiTW32xGvMbDKruymrA generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.pipesort import pipe_sort
from pipe2py.modules.pipeoutput import pipe_output

def pipe_8NMkiTW32xGvMbDKruymrA(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context.describe_input:
        return []

    forever = pipe_forever()


    sw_35 = pipe_fetch(
        context, forever, conf=dict(URL=[dict(type='url', value='file://data/www.fourtitude.com_news_publish_rss.xml'), dict(type='url', value='file://data/feeds.gawker.com_jalopnik_full.xml'), dict(type='url', value='file://data/www.autoblog.com_rss.xml')]))

    sw_54 = pipe_filter(
        context, sw_35, conf=dict(COMBINE=dict(type='text', value='or'), MODE=dict(type='text', value='permit'), RULE=[dict(field=dict(type='text', value='description'), value=dict(type='text', value='Porsche'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Mercedes'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='BMW'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Audi'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='VW'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Lamborghini'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Ferrari'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Pagani'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Aston'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='Lotus'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='TVR'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='description'), value=dict(type='text', value='AMG'), op=dict(type='text', value='contains'))]))

    sw_105 = pipe_sort(
        context, sw_54, conf=dict(KEY=[dict(field=dict(type='text', value='pubDate'), dir=dict(type='text', value='DESC'))]))

    _OUTPUT = pipe_output(
        context, sw_105, conf=dict())

    return _OUTPUT


if __name__ == "__main__":
    context = Context()
    pipeline = pipe_8NMkiTW32xGvMbDKruymrA(context, None)

    for i in pipeline:
        print i
