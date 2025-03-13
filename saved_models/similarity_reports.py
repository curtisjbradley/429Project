import pandas as pd
from ctgan import CTGAN
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
import sys
from plotly.graph_objects import Figure

model = "10"
real_data = pd.read_csv('../KDDTrain+.txt')
generated_data = pd.read_csv(model + ".csv")
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_data)

quality_report = evaluate_quality(
    real_data,
    generated_data,
    metadata)

plot = quality_report.get_visualization(property_name='Column Pair Trends')

new_fig = Figure(data=[plot.data[1]])

new_fig.update_layout(
    coloraxis2=plot.layout.coloraxis2,
    xaxis2=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        title=None,
        ticks="",
    ),
    yaxis2=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        title=None,
        ticks="",
    ),
    title=dict(
        text=f"Numerical Correlation (Dataset)",
        x=0.5,
        xanchor="center"
    ),
    height=500,
    width=500,
)

new_fig.write_image("real.png")
