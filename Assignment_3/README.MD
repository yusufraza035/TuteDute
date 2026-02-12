# Flask API & MongoDB Atlas Integration Project

## 📖 Project Overview

This project demonstrates:

1.  Creating a Flask API route that reads data from a backend JSON file
    and returns it as a JSON response.
2.  Creating a frontend form that submits data to MongoDB Atlas.
3.  Redirecting to a success page upon successful submission.
4.  Displaying error messages on the same page if submission fails.
5.  Using a .env file to securely store the MongoDB connection string.

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   Flask
-   MongoDB Atlas
-   PyMongo
-   python-dotenv
-   HTML

------------------------------------------------------------------------

## 📁 Project Structure

flask_project/ 
│ 
├── app.py 
├── data.json 
├── .env 
├── .gitignore 
├──requirements.txt 
└── templates/ 
   ├── form.html 
   └── success.html

------------------------------------------------------------------------


pip install flask pymongo dnspython python-dotenv

------------------------------------------------------------------------

### 5️⃣ Create `.env` File

MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/studentDB

------------------------------------------------------------------------

## ▶️ Run the Application

python app.py

Open in browser: http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🔗 Available Routes

### `/api`

-   Reads data from `data.json`
-   Returns JSON response

### `/`

-   Displays HTML form

### `/submit`

-   Inserts form data into MongoDB Atlas
-   Redirects to `/success` on success
-   Shows error message on failure

### `/success`

-   Displays "Data submitted successfully"

------------------------------------------------------------------------

## 📌 Conclusion

This project demonstrates backend API creation, frontend form handling,
database integration using MongoDB Atlas, error handling, and secure
configuration using environment variables.

------------------------------------------------------------------------

## 👨‍💻 Author

Sayyed yusuf raza
