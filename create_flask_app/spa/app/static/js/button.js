async function get_num() {
    const host = "http://" + window.location.host;

    // making a post request to the server
    const response = await fetch(host, {
        method: "POST"
    });

    // getting the json response
    const json_data = await response.json();

    // put number in the html
    const number = json_data.random_num;

    const p_find = document.getElementsByTagName("P");
    const p = p_find.length > 0 ? p_find[0] : document.createElement("p");

    document.body.appendChild(p);

    p.innerText = number;

}
