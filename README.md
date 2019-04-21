# Searchable School Suspension Database
A search tool I made for the Columbia Missourian's story on racial disparities in school suspensions in Missouri. I was responsible for cleaning the data and developing the interactive using Django.
## Data
A reporter submitted an open records request to get a database of suspensions given in Missouri from 2008 - 2017, broken down by year, grade level, school district, in-school/out-of-school, suspension length. I used an R script to summarize the data by year, race and schoool district.
## Interactive
I used the Python web framework Django to build a simple search tool so that users could see all of the suspensions given in a district for each year. 
I originally built a custom front-end, but instead decided that it would be better to use a wrapper template provided by the Missourian's CMS
