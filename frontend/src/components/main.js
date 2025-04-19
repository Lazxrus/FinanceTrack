// equivalen to http://127.0.0.1:5000/api/transactions
const API_URL = "/api/transactions";

// DOMContentLoaded means wait until the entire HTML is loaded before running any code.
document.addEventListener("DOMContentLoaded", () => {
    // We call loadTransactions() immediately to load existing transactions from the API.
    loadTransactions();

    //This listens for a submit event when the user clicks "Add".
    document.getElementById("transactionForm").addEventListener("submit", async (e) => {
        // e.preventDefault(); prevents the page from refreshing when the form submits (which is default browser behavior).
        e.preventDefault();

        // .value gets whatever the user typed into the input fields.
        const description = document.getElementById("description").value;
        const amount = parseFloat(document.getElementById("amount").value);
        // ^ parseFloat() ensures that the amount is treated as a number instead of a string
        const category = document.getElementById("category").value;

        //makes an HTTP request to Flask.
        const response = await fetch(API_URL, {
            // tells Flask that we want to send new data.
            method: "POST",
            headers: {
                // ensures Flask understands that we're sending JSON.
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ description, amount, category })
        });

        // checks if the API successfully added the transaction.
        if (response.ok) {
            // Clears form
            document.getElementById("transactionForm").reset();
            // Reload the table
            loadTransactions();
        } else {
            alert("Failed to add transaction.");
        }
    });
});

async function loadTransactions() {
    // sends a GET request to Flask.
    const response = await fetch(API_URL);
    // converts the response into JavaScript objects.
    const data = await response.json();

    // This ensures that the table doesn’t keep adding duplicate rows each time we reload transactions.
    const tableBody = document.getElementById("transactionsBody");
    tableBody.innerHTML = "";

        // loops through all transactions received from Flask.
    data.forEach((t) => {
        const row = `
            <tr>
                <td>${t.description}</td>
                <td>$${t.amount.toFixed(2)}</td> // formats the amount to 2 decimal places
                <td>${t.category}</td>
                <td>${t.date}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
        // adds the new row to the table.
    });
}
