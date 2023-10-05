# Final Project Proposal

I would like to use the dataset Crime Data from 2020 to Present, a dataset that reflects incidents of crime in the City of Los Angeles from 2020 to the present. As a resident of North Hollywood in Los Angeles County, I am very curious to uncover valuable insights into crime patterns in Los Angeles.

You can access the dataset here: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8

The API endpoint is available at https://data.lacity.org/resource/2nrs-mtv8.json

## Research Questions:

Here are the questions I aim to address:

1. Crime by Month:

When are crimes most prevalent throughout the year?

2. Crime by Time of Day:

What times of the day witness higher crime incident rates?

3. Crime by Location:

Which areas experience the highest rates of crime?

4. Types of Crime:

What are the most common crime types, and how frequently do they occur?

5. Gender Disparities in Crime:

Do females face a higher likelihood of becoming crime victims compared to males?

6. Age of Victims:

What are the mean, median, and mode ages of crime victims?

7. Ethnicity and Crime:

Which ethnic groups are most affected by crime?

8. Crime Locations:

Where do crimes typically occur, such as on the streets, in vehicles, buildings, or in the outskirts of the city?

9. Weapons Used in Crimes:

Are weapons commonly employed in these incidents, and if so, which types are prevalent?

10. Crime Resolution Rate:

What is the percentage of solved cases versus open cases?

11. Response Times:

Examine the average response times of law enforcement to different types of incidents.

## How I am planning to approach the research questions:

### Crime by Month:

- Retrieve the dataset using the provided API endpoint.
- Extract the date information and group incidents by month.
- Calculate the crime rate for each month.
- Visualize the results using a bar chart or line graph to identify trends.

### Crime by Time of Day:

- Extract the time information from the dataset.
- Group incidents by time of day (e.g., morning, afternoon, evening, night).
- Calculate the frequency of incidents for each time period.
- Create a visualization to show when crime incidents are most prevalent.

### Crime by Location:

- Analyze the location data (e.g., street, city, outskirts) in the dataset.
- Determine which locations have the highest crime rates.
- Visualize the distribution of crime incidents on a map or through charts.

### Types of Crime:

- Categorize crime incidents based on their type (e.g., theft, assault, burglary).
- Calculate the occurrence of each crime type.
- Create a bar chart or pie chart to display the distribution of crime types.

### Gender Disparities in Crime:

- Analyze the dataset to identify the gender of victims.
- Compare the number of male and female victims.
- Calculate the percentages and create visualizations for comparison.
- Further analyze the data to investigate whether certain types of crimes exhibit more pronounced gender disparities than others.

### Age of Victims:

- Extract the age information of victims from the dataset.
- Calculate the mean, median, and mode of victim ages.
- Visualize the age distribution of victims using histograms or box plots.

### Ethnicity and Crime:

- Analyze the dataset for information on the ethnicity of victims.
- Determine which ethnicities experience the most crime.
- Create visualizations, such as bar charts or pie charts, to represent the findings.
- Further analyze the data to investigate whether specific types of crimes exhibit more pronounced disparities among ethnic groups.

### Weapons Used in Crimes:

- Identify incidents where weapons were used.
- Categorize the types of weapons used.
- Calculate the frequency of each weapon type.
- Create a bar chart or pie chart to show the most commonly used weapons.

### Crime Resolution Rate:

- Differentiate between solved and open cases.
- Calculate the percentage of solved cases.
- Visualize this information through a pie chart or bar chart.

### Response Times:

- Calculate the response time for each incident by subtracting the reported timestamp from the response timestamp.
- Calculate mean, median, and standard deviation, for response times within each category.
- Create:
  - Box plots: Show the median, quartiles, and potential outliers in response times.
  - Histograms: Display the frequency distribution of response times.
  - Bar charts: Compare average response times across incident types.
