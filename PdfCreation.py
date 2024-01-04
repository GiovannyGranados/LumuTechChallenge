import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.platypus import Table, TableStyle
import scipy.stats
import pandas


def savePdfGenerated(initialData, finalDataFrame):
    pdf_file = "reports/report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=reportlab.lib.pagesizes.letter)

    c.setTitle("Bacon Ipsum JSON API Cosummer Analysis For Lumu")
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 770, "Bacon Ipsum JSON API Cosummer Analysis For Lumu")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(10, 750, "Initial Data")
    c.setFont("Helvetica", 10)
    L = simpleSplit(initialData,"Helvetica", 10, 600)
    y=730
    for t in L:
        c.drawString(10,y,t)
        y -= c._leading
    c.showPage()
    y=770

    c.setFont("Helvetica-Bold", 12)
    c.drawString(10, (y-5), "Exploratory Text Analysis")
    y -= c._leading
    c.setFont("Helvetica", 10)
    c.drawString(10, (y-5), "Below are the first ten data points sorted by count and length, respectively")
    y -= c._leading + 5
    createDataTable1(c, y, finalDataFrame)
    y = createDataTable2(c, y, finalDataFrame)
    #y = pageValidator(c, y, 10)
    c.drawString(10, (y-10), "Some key statistics")
    y -= c._leading + 5
    y = keyStatistics(c, y, finalDataFrame)
    y -= c._leading + 5
    c.showPage()
    y=770
    height = 300
    c.drawString(10, y, "Barplot")
    y -= c._leading + 5
    c.drawImage('plots/barPlot.png', x=100, y=y-height, width=400, height=height)
    y -= c._leading + 5 + height
    c.drawString(10, y, "Normal Distribution")
    y -= c._leading + 5
    c.drawImage('plots/NDPlot.png', x=100, y=y-height, width=400, height=height)
    y -= c._leading + 5 + height
    c.save()

def createDataTable1(c, y, finalDataFrame):
    df_transposed = finalDataFrame.T
    sortedFinalDataFrame = finalDataFrame.sort_values(by='Count', ascending=False)
    sortedFinalDataFrame = sortedFinalDataFrame.head(15)
    tableData = [sortedFinalDataFrame.columns.tolist()] + sortedFinalDataFrame.values.tolist()
    table = Table(tableData)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
    ]))
    tableWidth = 10  
    tableHeight = len(tableData) * 18  

    table.wrapOn(c, tableWidth, tableHeight)
    table.drawOn(c, 10, y - tableHeight)

def createDataTable2(c, y, finalDataFrame):
    df_transposed = finalDataFrame.T
    sortedFinalDataFrame = finalDataFrame.sort_values(by='Length', ascending=False)
    sortedFinalDataFrame = sortedFinalDataFrame.head(15)
    tableData = [sortedFinalDataFrame.columns.tolist()] + sortedFinalDataFrame.values.tolist()
    table = Table(tableData)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
    ]))
    tableWidth = 10  
    tableHeight = len(tableData) * 18  

    table.wrapOn(c, tableWidth, tableHeight)
    table.drawOn(c, 200, y - tableHeight)
    y -= tableHeight + 5 
    return y

def keyStatistics(c, y, finalDataFrame):
    data = [
        {'keyStatistics': 'Mean', 'Length': scipy.stats.gmean(finalDataFrame['Length']).round(2), 'Count': scipy.stats.gmean(finalDataFrame['Count']).round(2)},
        {'keyStatistics': 'StandardDeviation', 'Length': scipy.stats.tstd(finalDataFrame['Length']).round(2), 'Count': scipy.stats.tstd(finalDataFrame['Count']).round(2)},
        {'keyStatistics': 'Mode', 'Length': scipy.stats.mode(finalDataFrame['Length']).mode, 'Count': scipy.stats.mode(finalDataFrame['Count']).mode}
    ]
    keyStatisticsDF = pandas.DataFrame(data)
    tableData = [keyStatisticsDF.columns.tolist()] + keyStatisticsDF.values.tolist()
    table = Table(tableData)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
    ]))
    tableWidth = 300  
    tableHeight = len(tableData) * 18  

    table.wrapOn(c, tableWidth, tableHeight)
    table.drawOn(c, 10, y - tableHeight)
    y -= tableHeight + 5
    return y

def pageValidator(c, y, height):
    if y < height:
        c.showPage()
        y=770
    return y

    