import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import math
import datetime as dt
import pickle
import sklearn
import statsmodels

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc, dash_table
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State, ClientsideFunction



def sumar(numero1, numero2):
    """
    Realiza la suma de dos números.

    Args:
        numero1 (int): Primer número.
        numero2 (int): Segundo número.

    Returns:
        int: Resultado de la suma.
    """

    import glob
    paths_dictionaries = glob.glob('inicio/Insumos/Diccionarios_Covariables/*')
    paths_models = glob.glob('inicio/Insumos/Models/*')
    paths_pronos_base = glob.glob('inicio/Insumos/Pronos_Base/*.txt')

    objects = []
    for path in paths_dictionaries:
        with (open(path, "rb")) as openfile:
            while True:
                try:
                    objects.append(pickle.load(openfile))
                except EOFError:
                    break
    D = objects
    D2 = {}
    for elem in D:
        new_elem = list(elem[0].keys())[0]
        s = new_elem.split('_')
        elem[0][new_elem]['transf'] = s[0]
        D2['_'.join(s[1:-1])] = elem[0][new_elem]
    D2
    productos = {}

    for path in paths_pronos_base:
        print(path)

        name = '_'.join(path.split('/')[3].split('_')[:-1])
        print(name)
        path_model = 'inicio/Insumos/Models/{}.sav'.format(name)
        with (open(path_model, "rb")) as openfile:
            temp_model = pickle.load(openfile)
        productos[name] = {'pronos_base': pd.read_csv(path, delimiter = '\t'),
                            'feat_dict': D2[name],
                            'models': temp_model}
    data = pd.read_csv('inicio/Insumos/variables_exog.txt', delimiter = "\t")
    data['Fechas'] = pd.to_datetime(data['Fechas'],format='%d/%m/%Y')

    data.set_index('Fechas', inplace=True)
    # for c in data.columns:
    #     data[c] = data[c].apply(lambda x: float("{:.2f}".format(x)))
    data.tail()
    try:
        return data
    except (ValueError, TypeError):
        raise ValueError("Ambos valores deben ser números válidos.")
