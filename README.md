# Content-Curation: Finance/Securities 📈💰

## Project Overview 🚀

In light of the misinformation surrounding financial securities after the GameStop incident, this project aims to provide a reliable content curation service for both technical and non-technical users. The service offers updates on subscribed securities through an HTTP API for technical users and via email for non-technical users. Users can define the frequency of updates (daily or weekly) and create a portfolio of stocks to subscribe to. The service also provides access to market data for stocks and cryptocurrencies, as well as a popular portfolio feature.

## Features 🔍

- **HTTP API for Technical Users:** Technical users can subscribe to securities and receive updates through an HTTP API. They can define the frequency of updates and access market data for stocks and cryptocurrencies.
- **Email Subscription for Non-Technical Users:** Non-technical users can subscribe to securities and receive updates via email. They can also define the frequency of updates and access market data.
- **Portfolio Management:** Users can create a portfolio of stocks to subscribe to, determining the securities for which they receive updates.
- **Digests:** Daily and weekly digests are provided, including credible news on subscribed securities. The digests may capture portions of the original articles and link directly to the source to avoid redundancy and 'stealing news'.
- **Popular Portfolio:** A popular portfolio feature captures the most popular stocks per day, available for public viewing on a website.

## Usage 🛠️

1. **Technical Users:** Obtain an API key to access the service. Subscribe to securities and configure the frequency of updates using the HTTP API.
2. **Non-Technical Users:** Subscribe to securities and configure the frequency of updates via email.
3. **All Users:** Define a portfolio of stocks to receive updates for. Access daily and weekly digests for subscribed securities. View the latest available visual snapshots of the popular portfolio and the daily digest on a public website.

## Getting Started 🏁

To get started with the content curation service:

1. Register for an account on the service website.
2. Subscribe to securities and configure your preferences for updates.
3. Access the service via the HTTP API or email, depending on your user type.

## Technologies Used 💻

- **Django:** Web framework for building the service website.
- **API:** HTTP API for technical users to access the service.
- **Email Service:** Integration for sending updates to non-technical users via email.
- **Market Data:** Integration for accessing market data for stocks and cryptocurrencies.
- **Database:** Storage for user portfolios and subscription preferences.

## Cloning and Contributing 🚧

If you'd like to contribute to this project, follow these steps to clone the repository and set up your development environment:

### Cloning the Repository

1. **Clone the Repository:**
   ```
   git clone https://github.com/tshamala-pathy/Content-Curation.git

2. **Navigate to the Project Directory:**

    cd securities_finance

3. Setting Up the Project Locally
Install Dependencies:

bash
```
   pip install -r requirements.txt
```


Apply Migrations:


```
python manage.py migrate
```

Create a Superuser:


```
python manage.py createsuperuser
```

Follow the prompts to create a superuser account, which you can use to access the Django admin interface.

Run the Development Server:


```
python manage.py runserver
```

Access the Application:
Open your web browser and navigate to  
```
http://127.0.0.1:8000/
```
to view the application.

Contributing to the Project
Fork the Repository:
Click on the "Fork" button on the GitHub repository page to create a fork of the project under your GitHub account.

Clone the Forked Repository:
Clone the forked repository to your local machine using the git clone command as shown earlier.

Create a New Branch:


```
git checkout -b feature-branch
```

Replace feature-branch with a descriptive name for your branch.

Make Changes:
Make your desired changes to the codebase.

Commit Changes:

```
git add .
```
```
git commit -m "Your commit message"
```

Replace Your commit message with a brief description of the changes you made.

Push Changes:

```
git push origin feature-branch
```

Create a Pull Request:

Go to your forked repository on GitHub.
Click on the "Compare & pull request" button next to your feature branch.
Provide a title and description for your pull request.
Click on the "Create pull request" button to submit your changes for review.
We welcome contributions from the community to improve this project!

## Conclusion 🎉

The content curation service for finance/securities aims to provide reliable and timely updates for users interested in financial securities. By catering to both technical and non-technical users, the service ensures that users can access accurate information and make informed decisions regarding their investments.
