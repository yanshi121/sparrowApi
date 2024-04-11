from aparrowApi import SparrowApi
from aparrowApi import return_html
from aparrowApi import ContentType
app = SparrowApi(__name__)


@app.get('/test', content_type=ContentType.HTML)
def hello_world(args):
    print(args)
    return return_html(r"test.html")


@app.route("/", content_type=ContentType.JSON)
def hello_world(headers):
    return {"headers": headers}


app.run()

