// Waits until the DOM is ready
$(document).ready(function() {
    $("#go").click(() => {
        console.log($("#go").text())

        $.ajax({
            // url to send the request to (root address)
            url: lists_url,

            // type of the request
            type: "get",

            // type of the content sent
            contentType: "application/json",

            // data to send
            data: {
                button_text: $(this).text()
            },

            // code to execute on success
            success: (response) => {
                $("#go").text(response.seconds)
                $("#left-list").append(`<li class="card my-3 text-dark"> ${response.seconds} </li>`)
            }
        })
    })

    // Event when we click on <li> inside #left-list
    $("#left-list").on("click", "li", () => {
        $.ajax({
            url: lists_url,
            type: "post",
            contentType: "application/json",
            data: JSON.stringify({
                text: $(this).text()
            }),

            success: (response) => {
                $("#right-list").append(`<li class="card my-3 text-dark"> ${response.data} </li>`)
            }
        })
    })
})