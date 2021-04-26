#created function to get_data
#to use this function, please call the data source first
#look at the 2019-Annual.csv Measure Name column for data
#input data with keyword
#csv file will then be generated into data_sources folder
def get_data(keyword):
    import pandas as pd
    obesity_rawdata = pd.read_csv("data_sources/2019-Annual.csv")
    obtained_df = (obesity_rawdata.loc[(obesity_rawdata['Measure Name'] == keyword)])
    obtained_df.to_csv(f'data_sources\obtained_data_{keyword}.csv',index = False, header=True)
    #data extract to CSV, can then be imported for use

#call function prerequisite- from fx_list import get_data
#using function get_data('Your keyword')


#created correlation function so can be reused
#input x for x-axis, y for y-axis
#for annotation, i for x-axis position,j for y-axis position
def correlation(x, y, i, j):
    import matplotlib.pyplot as plt
    import scipy.stats as sts
    correlation = sts.pearsonr(x, y)
    slope, c_int, r, p, std_err = sts.linregress(x, y)
    fit = slope * x + c_int
    line_equation = f'y = {str(round(slope,2))}x + {str(round(c_int,2))}'
    plt.annotate(line_equation,(i,j),fontsize=13,color='black')
    plt.plot(x,fit,':r')
    print(f'The correlation between both factors is {round(correlation[0],2)}')

#call function prerequisite- from fx_list import get_data
#using function correlation(x,y,i,j)