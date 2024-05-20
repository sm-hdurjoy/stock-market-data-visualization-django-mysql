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
   cd learn-nest-frontend

   ```

3. Install the dependencies:
   ```bash
   npm install
   ```

### Running the Application

1. Start the JSON Server with authentication:

   ```bash
   json-server --watch data/db.json -m ./node_modules/json-server-auth -r data/routes.json --port 8000

   ```

2. Start the React application:

   ```bash
   npm run start

   ```

3. Open your browser and navigate to `http://localhost:3000`

### Project Structure

- `public` : Public assets
- `src` : Contains the source code
  - `assets` : Static assets like images and fonts
  - `components` : Reusable components
    - `Elements` : Basic UI elements
    - `Layouts` : Layout components
    - `Others` : Miscellaneous components
    - `Sections` : Section-specific components
  - `context` : Context API for state management
  - `hooks` : Custom React hooks
  - `pages` : Different pages of the application
    - `Cart`
      - `Components` : Components specific to the Cart page
    - `Dashboard`
      - `Components` : Components specific to the Dashboard page
    - `Home`
      - `Components` : Components specific to the Home page
    - `Order`
      - `Components` : Components specific to the Order page
    - `Products`
      - `Components` : Components specific to the Products page
  - `reducers` : Reducers for state management
  - `routes` : Application routing
  - `services` : Services for API calls
- `data` : JSON Server data files

### Deployment

The application is deployed using Netlify and Render. Follow these steps to deploy your own version:

1. Create an account on Netlify/Render.
2. Connect your GitHub repository to the deployment platform.
3. Configure the build settings:
   - Build command: `npm run build`
   - Publish directory: `build`
4. Deploy the site.