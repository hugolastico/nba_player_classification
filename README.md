# NBA Player Classification
The objective of this project is to provide a classifier to predict that a player is worth investing in because he will last more than 5 years in the NBA based on the sports statistics contained in the nba_logreg dataset. This model is designed to advise investors looking to capitalize on future NBA talent.

The parameters of the dataset are described below:

![Capture d’écran 2025-01-06 140946](https://github.com/user-attachments/assets/6c68adee-ddd8-4201-8b41-540050e38b14)

The **test.ipynb** file is the notebook used to explore the data and build the prediction model.

Once all the cells in this notebook have been launched, it will generate 2 files : 
- **scaler.plk**, for scaling the data the user fills in on the form
- **lda_model.plk**, which is the trained model.

The **test_app**.py file is used to launch a Flask API that enables the trained model to be used to make predictions from data sent via an HTTP POST request.
The **form_post** file is a Python client that interacts with the Flask API launched in test_app.py to send user data via a form system.

To find out whether a player is worth investing in:
- Start the Flask server in a terminal with the following command: *python test_app.py*
- In another terminal, run this command: *python form_post.py*
- Enter the player performance requested in the form.
