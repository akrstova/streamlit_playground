import random
from datetime import datetime, timedelta

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import numpy as np


df = pd.DataFrame(
    {
        "Animal": ["Lion", "Elephant", "Giraffe", "Monkey", "Zebra"],
        "Class": ["Mammal", "Mammal", "Mammal", "Mammal", "Mammal"],
        "Habitat": ["Savanna", "Forest", "Savanna", "Forest", "Savanna"],
        "Lifespan (years)": [15, 60, 25, 20, 25],
        "Average weight (kg)": [190, 5000, 800, 10, 350],
    }
)


def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )
    selected_indices = list(np.where(edited_df.Select)[0])
    if selected_indices:
        first_selection = int(selected_indices[0])
        st.session_state["Animal"] = df_with_selections.iloc[first_selection, :]["Animal"]
        switch_page("Plot")


selection = dataframe_with_selections(df)
st.write("Your selection:")
st.write(selection)
