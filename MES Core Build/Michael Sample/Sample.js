let fs = require('fs')
//read template and create the string
let template = fs.readFileSync("template.xml").toString()
//create array of lines of data
let atad = fs.readFileSync("data.csv").toString().split("\n")

atad.forEach( (ln, rn) => {
	if(ln != "") {
		let fields = ln.split(",")
		let temp = template
		temp = temp.replace("%RungNumber%", rn)
			.replace(/%LINENUMBER%/g, fields[0])
		console.log(temp)
	}
})