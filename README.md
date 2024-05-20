# Stock Market Data Visualization

This repository contains a web application for visualizing stock market data. Built with Django and MySQL, it provides interactive charts and dashboards to analyze and track stock performance over time.

## Features

- Data Visualization: Interactive charts to visualize stock prices, volume, and other financial metrics.
- Responsive Design: User-friendly interface that works on both desktop and mobile devices.
- Real-Time Updates: Automatically fetch and display the latest stock market data from csv.
- Historical Data Analysis: View and analyze historical stock data to identify trends and patterns.

## Technologies Used

- Django: High-level Python web framework for rapid development.
- MySQL: Relational database management system.
- Chart.js: JavaScript library for creating responsive charts.
- Bootstrap: CSS framework for responsive and modern web design.

## Getting Started

### Prerequisites

- Python3
- MySQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sm-hdurjoy/stock-market-data-visualization-django-mysql.git
   ```

2. Navigate to the project directory:
   ```bash
   cd stock-market-data-visualization-django-mysql
   ```

3. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:
   ```bash
   python manage.py migrate
   ```

5. Set up MySQL database:
- Create a new MySQL database
- Update the `DATABASES` settings in `settings.py` with your MySQL configuration

6. Apply database migrations:
   ```bash
   pip install -r requirements.txt
   ```

7. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

### Running the Application

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000`