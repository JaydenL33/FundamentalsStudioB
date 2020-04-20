/* export function objectLoader(url) {
    var request = new XMLHttpRequest()
    var data;
    // These are just properties of the request
    // The request actually gets executed here.
    
    request.open('GET', url, false);
    request.send();
    data = request.response
    return(data);
} */

export function objectLoader(url) {
    
    // To Store our Information
    var data;
    // Create Object for GETRequest
    var request = new XMLHttpRequest();
    // Config for Get Request 
    request.open("GET", url, false);

    // Sends request over network
    request.send();
    
    // After it's recieved request, what does it do?
    request.onload = function() {
        if (request.status !== 200) { // analyze HTTP status of the response
            console.log(`Error ${request.status}: ${request.statusText}`); // e.g. 404: Not Found
        } else { // show the result
            data = request.response;
            console.log(`Done, got ${request.response.length} bytes`); // responseText is the server
        }
    };
    data = JSON.parse(request.response);
    return(data);
} 
