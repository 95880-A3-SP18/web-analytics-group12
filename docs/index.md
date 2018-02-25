# House leasing websites Analytics Project Proposal

## Who are our customers?

Our target customers are those who move to a new city or a new country and want to rent a new apartment in a place which they are not familiar with. 

## What are their needs? 
	
Because our customers are usually those who don’t have any ideas about the new city,  they not only need the fragmented information about specific apartments displayed on the website, but also require the integrated information about the apartments’ floor plan, condition, price and distance in the whole range.  
	
## What specific problem(s) will you solve?
	
Zillow is a good place to find apartments online if the customers have specific restrictions about the apartments they would like to rent in their minds. Under this condition, people can use the filter to find out which are the perfect match apartments. However, there are still a part of customers who need to know some informations first, such as the regional distribution of apartments, the safety issues in different areas, the price distribution of apartments and so on and so forth before they actually have their own preference and begin to use the filter to move to the next step of using the website. By collecting and analysing data like property types and price etc. we can provide the customers more information about the characteristics of different regions, which could help them get a generic idea of the city they are not familiar with. What our application does is to collect the data and integrate them into a visualized way in order to lead the target customers find their own criteria about apartments. 
 
## Why do these problems need solved?
	
Because of this problem, some user may change to use other apps with more guidance or even choose to ask friends for help without using online application to find a perfect match apartment. By solving this issue, the company can extend their active user and increase the profit.
	
## Where are you going to pull the data from?
	
Zillow , Craiglist or other rental websites.

# UI Wireframe Review
1.index page:
On top of the index page, there is a navbar. We support user register, login function. And a button for back-to-home page.
The main content of the index page is a dashboad including the following buttons linked to different functions. See below.

2. Price Trend page:
On this page , we provide the function of Price Trend. That is, a time series of average price change of houses in Pittsburgh area.
This is implemented using data visualization in python and the graph is generated from our django backend.

3.Price Distribution page:
On this page, we provide the function of Price Distribution. There is a map showing the price difference in different districts like Shadyside, Green Field or Squirrel hill. Map will be colored differently according to the price.

4.Search page:
This page provide the function of searching specific house resources using key word such as "two bed room" or anything that could be found in description.

5.Favorate page:
This page is a favorate list for user to keep a record of his favorate house resouces.

6.Message Board page:
This page is for user communicating and sharing house resources like selling or renting.

Please see the following screenshots.
![alt text](https://github.com/DongZuo/OfferHunter/blob/master/media/profile_images/index1.jpg "index1")
![alt text](https://github.com/DongZuo/OfferHunter/blob/master/media/profile_images/index2.jpg "index2")
