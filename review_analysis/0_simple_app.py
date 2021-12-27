import justpy as jp

def app():
    # create a QuasarPage instance or object
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="these graphs represent course review analysis")
    return wp

jp.justpy(app)