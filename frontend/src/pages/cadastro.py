from deta import Deta
import streamlit as st

DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("database")

class Account:
    def __init__(self, password):
        self.password = password

    def to_dict(self):
        return {"password": self.password}

def create_account():
    st.title("Account Creation")
    password_input = st.text_input("Create a password", type="password")
    create_button = st.button("Create Account")

    if create_button:
        if not password_input:
            st.error("Password cannot be empty.")
            return

        account = Account(password_input)
        account_data = account.to_dict()

        # Check if the account already exists
        result = db.get("account")

        if result:
            st.error("An account already exists.")
            return

        # Save the account in the database
        db.put(account_data, "account")
        st.success("Account created successfully!")
