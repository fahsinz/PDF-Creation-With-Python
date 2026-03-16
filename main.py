from reportlab.lib import colors  # Fix 1: Corrected import and spelling
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer, Paragraph, Table, SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing

doc = SimpleDocTemplate('report.pdf')
styles = getSampleStyleSheet()

title = Paragraph('Sales Report', styles['Title'])

sales_data = {
    'Alpha': [100, 120, 140, 120],
    'Beta': [70, 60, 60, 50],
    'Gamma': [200, 200, 200,340], 
}

table_data = [
    ['Product', 'Q1', 'Q2', 'Q3', 'Q4'],
    ['Alpha',] + sales_data['Alpha'],
    ['Beta',] + sales_data['Beta'],
    ['Gamma',] + sales_data['Gamma'],
]

table = Table(table_data, style=[
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey), # Fix 2: Changed to colors
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold')
])

chart = Drawing(400, 200)

bar_chart = VerticalBarChart()
bar_chart.data = [sales_data['Alpha'], sales_data['Beta'], sales_data['Gamma']]
bar_chart.categoryAxis.categoryNames = ['Q1', 'Q2', 'Q3', 'Q4']
bar_chart.valueAxis.valueMin = 0
bar_chart.valueAxis.valueMax = max(max(x) * 1.1 for x in bar_chart.data)
bar_chart.valueAxis.valueStep = 50

chart.add(bar_chart)

doc.build([title, Spacer(1, 12), table, chart])