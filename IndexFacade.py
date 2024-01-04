import DataAnalysis
import PdfCreation
from flask import Flask, send_from_directory


def dataPreparation(inputString):
    return DataAnalysis.dataCleaning(inputString)

def createPlots(inputDataFrame):
    DataAnalysis.createBarPlot(inputDataFrame)
    DataAnalysis.createNDPlot(inputDataFrame)

def createPdf(initialData, finalDataFrame):
    PdfCreation.savePdfGenerated(initialData, finalDataFrame)

