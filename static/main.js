// JS is responsible for fetching transactions from Flask and displaying them

const API_URL = "/api/transactions"; 
//API endpoint we send requests to
// equivalent to typing http://127.0.0.1:5000/api/transactions

//Run code after page loads
//DOMContentLoaded makes it wait until HTML is loaded before running any code
document.addEventListener("DOMContentLoaded", () => {
    loadTransactions();
})