# CB+ backend intern developer test   
# 1. Summary
You will be tasked with creating a minimal inventory app using Django.   
The information stored by the app is a list of references and their corresponding expiry date. In a    
shop an employee can for any reference, enter the current shortest expiry date present on the   
shelves.   
Example: a store sells a yogurt. On display, there are yogurts expiring on the 10 th of October and   
others expiring on the 13 th of October. The shortest expiry date is 10 th of October. So the app will   
give the information that the yogurts will expire on the 10 th of October.   
# 2. Requirements   
Create a Django application backed by a PostgreSQL database, which displays the current list of   
expiry dates for the products in the shop.   
The following features are expected:   
• Enter a new expiry date for a GTIN (the digits below the barcode)   
• Display a list of all current Expiry dates in the shop   
• When entering a GTIN already used, the app should detect the already existing reference and
update its expiry date.    
    
Optional features could be: sorting and filtering the list, a responsive design...    
You are responsible of designing the model and also the general design of the interface. It is required   
that the user interface is styled with CSS.   
# 3. Expected Result
1. Estimate the time needed to develop the app. Split this estimate in small tasks as needed.
Send us this estimate as soon as possible.    
2. Deploy the Django app on a serveur of your choice. Services like Heroku provide free hosting.    
3. Send us:   
a. The URL of the app   
b. A link to your remote git repository (needs to be public so we can clone it)   
c. An explanation of the process to build the app locally    
d. A short text explaining your technical decisions and possible areas of improvement.    
# 4.Evaluation criteria
1. Understanding of task to be performed
2. Respect of the deadline (2 days maximum)
3. Knowledge of the Django framework and of html / css
4. Quality of commits
