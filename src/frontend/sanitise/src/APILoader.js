export function ghibliapi() {
    var data;
    var request = new XMLHttpRequest()
    // These are just properties of the request
    request.onload = function() {
        // Begin accessing JSON data here
        if (this.readyState === 4 && this.status === 200) {
        data = JSON.parse(this.response)
        // data.forEach(sample => {
        //     // Log each movie's description
        //     console.log(sample.text)
        //   })
        console.log(data);
        }
        else {
            console.log("Error!")
        }
    }
    // The request actually gets executed here.
    request.open('GET', 'http://localhost:5000/test', true)
    
    request.send()
    return(data)
}