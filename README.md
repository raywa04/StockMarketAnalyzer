# Stock Market Dashboard

This project is a full-stack web application that provides real-time stock market data visualization. It uses a modern front-end with React and Bootstrap, and a back-end API built with Flask and Spark/PySpark for data processing. The application is containerized using Docker.

## Tech Stack

### Frontend
- React
- Bootstrap

### Backend
- Flask
- PySpark
- Pandas
- Matplotlib

### Containerization
- Docker
  
## Setup Instructions

### 1. Get an Alpha Vantage API Key

Sign up for an API key at [Alpha Vantage](https://www.alphavantage.co/). Replace `'your_alpha_vantage_api_key'` in `backend/scripts/data_processing.py` with your actual API key.

### 2. Install Frontend Dependencies

Navigate to the `frontend` directory and run:

bash
yarn install 

### 3. Build Docker Images

Navigate back to the project root directory and run:

docker-compose build

### 4. Run the Application

Start the application using Docker Compose:

docker-compose up

### 5. Access the Application

Open your web browser and navigate to http://localhost:3000/ to see the application.

### Contributing 
If you would like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

### License
This project is open source and available under the MIT License.



