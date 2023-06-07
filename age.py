from dash import html, Dash, dcc
from population import *
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use("Agg")
from dash.dependencies import Input, Output

def create_age_graph(name="Région de Bruxelles Capitale") :
    fig = plt.figure(figsize=(7, 5))
    
    population_df[name].plot.bar(color="g")
    plt.xticks(rotation="horizontal")

    plt.title(f"Répartition de la population par classe d'âge ({name})")
    plt.xlabel("Groupes d'âge")
    plt.ylabel("Part du groupe dans la population totale")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    img = base64.b64encode(buffer.getbuffer()).decode("utf8")
    buffer.close()
    plt.close(fig)
    return f"data:image/png;base64,{img}"


app = Dash(__name__)  
app.layout = html.Div([
    html.H1("Communes de Bruxelles"),
    html.Section([
        html.Div(dcc.RadioItems(
                                options= communes, 
                                value=communes[0], id="communes-filter")),

        html.Img(id="age-graph-img", src=create_age_graph())
    ], className="age-section")
])  

@app.callback(
    Output("age-graph-img", "src"),
    [Input("communes-filter", "value")]
)
def upgrade_age_graph(name) :
    return create_age_graph(name)

if __name__ == "__main__" :  
    app.run_server(debug=True)