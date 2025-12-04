# Employee Performance Analytics
 
Employee performance and the desire to optimise a labourforce towards higher productivity, is a topic at the lips of every business owner/runner. Traditional forms of encouraging employees towards higher productivity have been explored in length. Companies today spend a good amount of money in assessing productivity across different operational units, teams and departments as well.
 
# Dataset 
The labour force being one of the key drivers of overall company revenue, it is important to have a full understanding of what kind of insights we can collect from the assumed, as well as researched performance indicators; hence why the selected dataset for this project centres around HR performance analytics. The dataset can be accessed directly on the Kaggle platform.

link: https://www.kaggle.com/datasets/sanjanchaudhari/employees-performance-for-hr-analytics

 
# Data Size
The datasets contain 14 columns, most of the columns are related to traditional key indicators or measures, but do not have any modern measures/features. The data set has around 17,417 rows.  Actual shape of the dataset being (17417, 13).  The data-type ranges from numeric (8 columns) to object (5 columns). The overall memory usage stats are slightly over 1,7 mbs

 # Project Goals
In assessing employee data, companies can then utilise this information to make strategies that create some kind of competitive edge within the labour force, and respective field of operations. 

Having KPI and awards as our notable performance indicators, we can see if various predictors of performance can contribute to the success of mentioned performance indicators. 

Training of employees is seen as a necessary aspect of performance enhancement. Looking into the predictor, to see if the number of trainings has any influence on the training scores and KPIs would be useful for structuring:

		Hypothesis 1: Employees who attend more trainings have higher average training scores. 

		Hypothesis 2: Employees who met KPIs (> 80%) in the past year attend more trainings. 

Some departments have new hires in them, and since they are not as experienced as other members that have been employed longer, there is a possibility that performance is lowered as a result:

		Hypothesis 3: New hires have lower KPI achievement rates than tenured employees.

Efficiency and execution of goals, can mean needing a large labour force. For departments that are larger, there could be an advantage in respect to meeting KPI and having awards. They could also take up more trainings. 

		Hypothesis 4: Employees in larger departments have a higher number of   trainings.

# Project Structure
The project has four main folders. The Data folder contains uncleaned and cleaned csv files of the data set. The Notebooks folder has all the used notebooks in it. In the src folder are the scrips, and the reports folder contains the slides.  

# Project Structure
● How to Run 
○ Environment requirements (Python version, main libraries). 
○ How to install dependencies (pip install -r requirements.txt). 
○ How to run the main analysis (which notebooks/scripts to execute). 

# Results 
H1: The number of training sessions do not guarantee higher scores, this varies from person to person. Correlation here is very weak. 

H2: Surprisingly, more trainings correlate with slightly lower odds of meeting KPIs > 80

H3: There is no significant difference between the tenured employees and new hires when it comes to KPI goals being met, and average scores.

H4: There is a weak but positive indication that the larger the department, the higher the number of trainings. Meeting One’s KPIs is not really influenced by department size. However, the number of awards is influenced by department size.

# Key Insights

Quantity of training alone is not a reliable performance booster. Training programs may need personalisation, focusing on employees’ skill gaps rather than applying a “one-size-fits-all” approach. A proactive development approach might need to be assigned to employees that are underperforming, as opposed to throwing them into another training programme .

Performance is not strongly tied to experience within the company. Onboarding programs for new hires seem effective enough to bring them up to speed with experienced employees. Resources might be better spent on continuous performance support rather than assuming tenured staff always outperform newer employees.

Training allocation is influenced by departmental scale, this could be as a result of more resources or structured HR processes in larger teams (traditional company structure). KPI achievement not being directly linked to department size, suggests that team size alone doesn’t improve productivity. highlighting the importance of individual performance management. 

Awards being higher in bigger departments could mean recognition programs are scale based, and merit based, looking into this to ensure fair assessment, would be prudent for future HR policies within the company, where fairness is concerned. 


