import pandas
import matplotlib.pyplot 
import scipy.stats
matplotlib.pyplot.switch_backend('agg')

def dataCleaning(inputString):
    baseText = inputString.lower() 
    baseTextList = baseText.split()
    baseDataSeries = pandas.DataFrame(baseTextList, columns=['Data']) 

    baseDataSeries = baseDataSeries['Data'].str.replace(r'[^\w\s]', '', regex=True) 

    countDataSeries = baseDataSeries.value_counts()

    finalDataFrame = pandas.DataFrame({'Data': countDataSeries.index,'Length': countDataSeries.index.str.len(),'Count': countDataSeries.values})
    return finalDataFrame

def createBarPlot(finalDataFrame):
    barPlot = finalDataFrame.plot(kind='bar', x='Data', y='Count', color='skyblue')
    barPlot.tick_params(axis='x', labelsize=6)
    matplotlib.pyplot.title('Bacon Ipsum JSON API Word Count')
    matplotlib.pyplot.xlabel('Words')
    matplotlib.pyplot.ylabel('Count')

    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.savefig('plots/barPlot.png')
    matplotlib.pyplot.close()


def createNDPlot(finalDataFrame):
    mean = scipy.stats.gmean(finalDataFrame['Length'])
    sd = scipy.stats.tstd(finalDataFrame['Length'])
    matplotlib.pyplot.plot(finalDataFrame['Length'].sort_values(), scipy.stats.norm.pdf(finalDataFrame['Length'].sort_values(), mean, sd)) 
    matplotlib.pyplot.title('Normal Distribution of Lenght')
    matplotlib.pyplot.axvline(x=mean, color='r', linestyle='--')
    matplotlib.pyplot.text(3, 0, 'x={0}'.format(mean.round(2)), color='r')
    matplotlib.pyplot.savefig('plots/NDPlot.png')
    matplotlib.pyplot.close()



