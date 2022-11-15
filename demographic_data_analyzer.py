import pandas as pd

def calculate_demographic_data_analyzer(print_test = True):
    col_name = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
    df = pd.read_csv('adult_data.csv',sep=', ', names=col_name, engine='python')

    #How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
    race_count = df['race'].value_counts()

    #What is the average age of men?
    avg_male = round(df.loc[df['sex'] == 'Male','age'].mean(),0)

    #What is the percentage of people who have a Bachelor's degree?
    percentage_bachelor = round((df['education'].value_counts()[2]/df['education'].count()) * 100,1)

    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advance_edu = round((df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].count()/df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].count()*100)[0],1)

    #What percentage of people without advanced education make more than 50K?
    without_advance_edu = round((df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') & (df['salary'] == '>50K')].count()/df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].count())[0]*100,1)

    #What is the minimum number of hours a person works per week?
    min_work_hr = df['hours-per-week'].min()

    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    percentage_people_min_work_hr =df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].count()[0]/df.loc[df['hours-per-week'] == 1].count()[0]*100

    #What country has the highest percentage of people that earn >50K and what is that percentage?
    rich_country = (df.loc[(df['salary'] == '>50K'),'native-country'].value_counts()/df.loc[:,'native-country'].value_counts()*100).sort_values(ascending=False).index[0]
    percentage_rich_country = round((df.loc[(df['salary'] == '>50K'),'native-country'].value_counts()/df.loc[:,'native-country'].value_counts()*100).sort_values(ascending=False)[0],1)
    #Identify the most popular occupation for those who earn >50K in India.
    popular_job_in_India = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'),'occupation'].value_counts().keys()[0]

    if print_test==True :
        print("Number of each race:\n", race_count) 
        print("Average age of men:", avg_male)
        print(f"Percentage with Bachelors degrees: {percentage_bachelor}%")
        print(f"Percentage with higher education that earn >50K: {advance_edu}%")
        print(f"Percentage without higher education that earn >50K: {without_advance_edu}%")
        print(f"Min work time: {min_work_hr} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentage_people_min_work_hr}%")
        print("Country with highest percentage of rich:", rich_country)
        print(f"Highest percentage of rich people in country: {percentage_rich_country}%")
        print("Top occupations in India:", popular_job_in_India)

    return{
        'race_count': race_count,
        'average_age_men': avg_male,
        'percentage_bachelors': percentage_bachelor,
        'higher_education_rich': advance_edu,
        'lower_education_rich': without_advance_edu,
        'min_work_hours': min_work_hr,
        'rich_percentage': percentage_people_min_work_hr,
        'highest_earning_country': rich_country,
        'highest_earning_country_percentage': percentage_rich_country,
        'popular_job_in_India': popular_job_in_India
    }
