Documentation of this project 


This is the example of full stack application . Frontend and backend both , follpwing are the features of this application . 
1 -  you can add an item with UI in the database.
2 - You can update an item with UI in the database .
3 - you can see the count of the total items in the UI from the data base . 
4 - You can delete the item with UI in the database


Frontend :
We have used the nextjs framework to build the frontend with react library of making UI . 
To connect to the frontend you must come to the frontend folder .


1- If you are first time opening in your machine so you have to forst install the dependencies 
                      - npm install / npm i 


2 - if you have already once opened the frontend in your machine so u dont need to install the dependencies just open it .
                      - npm start 



---------------------------------------------------------------------------------------------------------------


Backend :
-We have used postgressql as a data base its driver is psycopg2. 

-Uvicorn as a server .

-Fastapi as a api .

-For the data base you have to have postgresql and pgadmin installed in your machine or in docker . pgadmin by default comes with postgresql . 

            - you have to manually make a database in the postgresql through pgadmin (pgadmin is the UI for the database)


-we have created the virtual environment for the backend ,to activate it   
            -fastapiproject\Scripts\Activate.bat 
   
    -if you are connecting server  first time so after activation of virtual environement u need to install depencies to install run this command 
            -pip install -r requirements.txt

            -you can also manually install all dependencies in the virtual environment 
               pip install sqlalchemy, fastapi, uvicorn , psycopg2

    -if you have connected it before this time and all the dependencies you have installed before it  so u need to just activate the virtual environment  and run this command  
            -uvicorn main:app --reload


-for the fastapi :    
    -if you want to check your api is working perfectly        
    -start the server run this command to start
        -uvicorn main:app --reload
    -Then whatever the IP address is given click it (ctrl+c) then type /docs with IP adress .
        -e.g : 0.0.0.8000/docs
    -it will drive you to the swagger page (there you can test your API)    





            


           