$(document).ready(function () {
    $("#card_form").on("submit", function (event) {
        event.preventDefault(); // prevent default form submission behavior
        let cartId = $(this).data()
        let data = $(this).serializeArray()
        data.push({name: "id", value: cartId['id']})
        console.log(data)
        $.ajax({
            url: "/app/card-update/",
            method: "POST",
            data: data, // send form data as serialized string
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



    $('#transactionForm').submit(function (event) {
        event.preventDefault(); // Зупиняємо стандартну поведінку кнопки
        var amount = $('#amountInput').val();
        var category = $('#categorySelect').val();
        var form = $(this).serializeArray()
        let cartId = $(this).data()
        // form.push({name: "type", value: type})
        form.push({name: "amount", value: amount})
        form.push({name: "category", value: category})
        form.push({name: "id", value: cartId['id']})
        console.log(form)
        // Виконуємо AJAX-запит до сервера для збереження транзакції
        $.ajax({
            url: '/app/add_transaction/',  // Замініть на відповідний URL вашого Django-виду
            method: 'POST',
            data: form,
            success: function (response) {
                // Успішна відповідь від сервера
                console.log(response["data"]);
                let card_balance = response['data']
                $(".fa-coins + span").text(card_balance)
                // Очищаємо поля форми після успішного створення транзакції
                $('#amountInput').val('0');
                $('#categorySelect').val('');

            },
            error: function (error) {
                // Помилка відповіді від сервера
                console.log(error); // Можна виконати додаткові дії, якщо потрібно
            }
        });
    })

    $("#add_card_form").on("submit", function (event) {
        event.preventDefault(); // prevent default form submission behavior
        let data = $(this).serializeArray()
        console.log(data)
        $.ajax({
            url: "new_card/",
            method: "POST",
            data: data, // send form data as serialized string
            success: function (response) {
                console.log(response);
                location.reload();

            },
            error: function (xhr, status, error) {
                console.log(status);
                console.log(error);
            }
        });
    });

});


