import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure

from cheese import *

cheese = Cheese()
app = Flask(__name__)


@app.route("/")
def dashboard():
    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(16,7))
    ax = fig.subplots(ncols=2)
    ax[0].plot(cheese.temperature)
    ax[0].set_ylabel("Temperatur in °C")
    ax[0].axhline(TEMPERATURE, color="g")
    ax[1].plot(cheese.humidity)
    ax[1].set_ylabel("Luftfeuchtigkeit in %")
    ax[1].axhline(HUMIDITY, color="g")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<center><h1>Käsekammer Dashboard</></><img src='data:image/png;base64,{data}' width=100%/>"