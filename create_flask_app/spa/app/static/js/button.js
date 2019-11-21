async function get_num() {
    const host = "http://" + window.location.hostname;

    // making a post request to the server
    const response = await fetch(host, {
        method : "POST"
    });

    // getting the json response
    const json_data = await response.json();

    // put number in the html
    const number = json_data.random_num;

    if (document.getElementsByTagName("p"))
        document.getElementsByTagName("p").parentNode.removeChild(document.getElementsByTagName("p"));
    var p = document.createElement("p");
    if (p.innerHTML){
        p.innerHTML = number;
        }
   
}
