function findOddNumber(arr) {
	loop: {
		for (var i=0; i<arr.length; i++) {
			var elem = arr[i];
			if ((elem % 2) != 0)
			{
				return "<h1> + elem is" + elem + "</h1>";
				break loop;
				console.log("Odd Number Found!")
			}
		console.log("No odd number found.")
		}

	}
	console.log("Done!")

}

var arr = [2, 4, 6, 8, 9];

document.getElementById("demo").innerHTML = findOddNumber(arr);