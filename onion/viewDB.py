from django.shortcuts import render
from django.views import View
import pandas as pd
from .models import Test
import plotly.graph_objects as go


class ViewFromDB(View):
    template_name = "onion_leafs/show_table_from_db.html"

    @staticmethod
    def generateGraph(graphData, title):
        # Convert date column to datetime
        graphData["date"] = pd.to_datetime(graphData["date"])

        # Convert numeric columns to appropriate data types
        graphData["high"] = graphData["high"].astype(float)
        graphData["low"] = graphData["low"].astype(float)
        graphData["open"] = graphData["open"].astype(float)
        graphData["close"] = graphData["close"].astype(float)
        graphData["volume"] = graphData["volume"].astype(int)

        # Filter data for the specified trade code
        filtered_data = graphData[graphData["trade_code"] == title]

        if filtered_data.empty:
            print(f"No data available for trade code '{title}'")
            return

        # Create the plotly figure
        fig = go.Figure()

        # Add traces for high, low, open, and close values with a separate y-axis
        fig.add_trace(
            go.Scatter(
                x=filtered_data["date"],
                y=filtered_data["high"],
                mode="lines+markers",
                name="High",
                yaxis="y1",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=filtered_data["date"],
                y=filtered_data["low"],
                mode="lines+markers",
                name="Low",
                yaxis="y1",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=filtered_data["date"],
                y=filtered_data["open"],
                mode="lines+markers",
                name="Open",
                yaxis="y1",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=filtered_data["date"],
                y=filtered_data["close"],
                mode="lines+markers",
                name="Close",
                yaxis="y1",
            )
        )

        # Add volume as a bar trace with a separate y-axis
        fig.add_trace(
            go.Bar(
                x=filtered_data["date"],
                y=filtered_data["volume"],
                name="Volume",
                opacity=0.5,
                yaxis="y2",
            )
        )

        # Update layout with separate y-axes
        fig.update_layout(
            title=f"Price and Volume Over Time for {title}",
            xaxis=dict(title="Date", tickangle=45),
            yaxis=dict(title="Price", side="left", position=0),
            yaxis2=dict(title="Volume", overlaying="y", side="right", position=1),
            legend=dict(x=0, y=1.1),
        )

        # Export as HTML
        fig.write_html("onion/templates/onion_leafs/plot_db.html")

    def get_from_db(self):
        qs = Test.objects.values(
            "date", "trade_code", "high", "low", "open", "close", "volume"
        )
        return qs

    def get(self, request, *args, **kwargs):

        data = self.get_from_db()
        trade_name = request.GET.get("trade")

        graphData = pd.DataFrame(list(data))

        self.generateGraph(graphData, trade_name)

        # Group by 'Trade_code' and calculate the mean value for each group
        mean_values = graphData.groupby("trade_code").mean()

        trade_codes = mean_values.index.tolist()
        title = [{"trade_code": code} for code in trade_codes]

        context = {"data": data, "title": title}

        return render(request, self.template_name, context)
