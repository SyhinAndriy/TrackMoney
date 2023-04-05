$("#card_form").on("submit", function (event) {
    event.preventDefault(); // prevent default form submission behavior
    $.ajax({
        url: "/app/card-update/",
        method: "POST",
        data: $(this).serialize(), // send form data as serialized string
        success: function (response) {
            console.log(response);
            let card_balance = response['data']
            $(".fa-coins + span").text(card_balance)
        },
        error: function (xhr, status, error) {
            console.log(status);
            console.log(error);
        }
    });
});


// select the transaction type buttons and category select
const transactionTypeButtons = document.querySelectorAll('.transaction-type-button');
const categorySelect = document.getElementById('categorySelect');

// create an object with available categories for each transaction type
const categories = {
    expenseBtn: ['Category 1', 'Category 2', 'Category 3'],
    profitBtn: ['Category 4', 'Category 5', 'Category 6'],
    transferBtn: ['Category 7', 'Category 8', 'Category 9']
};

// function to update the category select options based on the selected transaction type
function updateCategoryOptions() {
    // get the selected transaction type
    const selectedType = document.querySelector('.transaction-type-button.active').id

    // get the categories for the selected type
    const typeCategories = categories[selectedType];

    // clear the current options from the category select
    categorySelect.innerHTML = '';

    // add new options for each category in the selected type
    typeCategories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.text = category;
        categorySelect.add(option);
    });
}

// add click event listeners to the transaction type buttons to update category options
transactionTypeButtons.forEach(button => {
    button.addEventListener('click', () => {
        // remove active class from all buttons
        transactionTypeButtons.forEach(button => {
            button.classList.remove('active');
        });
        // add active class to the clicked button
        button.classList.add('active');

        // update category select options
        updateCategoryOptions();
    });
});

// call the function initially to set the category options based on the default selected type
updateCategoryOptions();

