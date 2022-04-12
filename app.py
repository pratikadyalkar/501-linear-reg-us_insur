import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State



########### Define your variables ######
myheading1='Predict Your Insurance Premium'
image1='dataset-cover.jpeg'
tabtitle = 'In-sure'
sourceurl = 'https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset'
githublink = 'https://github.com/pratikadyalkar/501-linear-reg-us_insur'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H3('Insurer Details:'),
                html.Div('Age:'),
                dcc.Input(id='Age', value=27, type='number', min=18, max=75, step=1),
                html.Div('BMI'),
                dcc.Input(id='BMI', value=14, type='number', min=14, max=60, step=1),
                html.Div('Female:'),
                dcc.Input(id='Female', value=1, type='number', min=0, max=1, step=1),
                html.Div('Male:'),
                dcc.Input(id='Male', value=0, type='number', min=0, max=1, step=1),
                html.Div('Smoker:'),
                dcc.Input(id='Smoker', value=0, type='number', min=0, max=1, step=1),
                html.Div('Non-Smoker:'),
                dcc.Input(id='NonSmoker', value=1, type='number', min=0, max=1, step=1),

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Insurance Premium:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:'),
    html.Div('Predicted Price = (5.8229115397391016e+16 Baseline) + (247.8943 * age) + (312.6561 * bmi) + (5.311799153163519e+16 * female) + (5.311799153163498e+16 * male) + (5111123865767279 * smoker) + (5111123865744300 * non-smoker)'),
    # html.Br(),
    # html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='Age', component_property='value'),
    State(component_id='BMI', component_property='value'),
    State(component_id='Female', component_property='value'),
    State(component_id='Male', component_property='value'),
    State(component_id='Smoker', component_property='value'),
    State(component_id='NonSmoker', component_property='value')

)
def ames_lr_function(clicks, age,bmi,female,male,smoker,nonsmoker):
    if clicks==0:
        return "waiting for inputs"
    else:
        y = [-58229115397391016  + 247.8943 * age + 312.6561 * bmi + 5311799153163519 * female + 5311799153163498 * male + 5111123865767279 * smoker + 5111123865744300 * nonsmoker]
        #y = [-1360501.3809 + 704.4287*YearBuilt + 12738.4775*Bathrooms + -7783.1712*BedroomAbvGr + 49.824*TotalSF+ 25282.091*SingleFam+ -6637.2636*LargeNeighborhood]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
