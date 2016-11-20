function showUser() {
	var string = "Prijavljen kot: ";
	document.getElementById('prijavljen').innerHTML = string + document.getElementById("user_ime").value;
	document.getElementById('prijavljen').display = true;
}

function dodajNapravo() {
	var parentDiv = document.getElementById("mainOkno");
	var iDiv = document.createElement("div");
	//iDiv.id = "block";
	iDiv.className = "dataContainer";
	parentDiv.appendChild(iDiv);
	
	var figure = document.createElement('figure');
	iDiv.appendChild(figure);
	
	var img = document.createElement("img");
	img.src = "gglass.jpg";
	img.style.width = 160 + 'px';
	img.style.height = 160 + 'px';
	figure.appendChild(img);
	
	var jDiv = document.createElement("div");
	jDiv.className = "dataEl";
	iDiv.appendChild(jDiv);
	
	var h = document.createElement("h3");
	var imeNaprave = document.getElementById("id_naprave").value;
	var appendText = document.createTextNode(imeNaprave);
	h.appendChild(appendText);
	jDiv.appendChild(h);
	
	var list = document.createElement("ul");
	var table = document.getElementById("id_tech");
	for (var i = 0, row; row = table.rows[i]; i++) {
		var liText = document.getElementsByName("ts")[i].value;
		if(!liText.length == 0) {
			var li = document.createElement("li");
			var appendText = document.createTextNode(liText);
			li.appendChild(appendText);
			list.appendChild(li);
		}
	}
	
	jDiv.appendChild(list);
	
	var det = document.createElement("details");
	
	var dodatno = document.getElementById("dodatenOpis").value;
	var x = document.createTextNode(dodatno);
	var p = document.createElement("p");
	if(!dodatno.length == 0) {
		p.appendChild(x);
		det.appendChild(p);
	}
	
	jDiv.appendChild(det);
}