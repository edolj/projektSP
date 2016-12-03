function redirectReg() {
	window.location.href='registration.html';
}

function search(ele) {
    if(event.keyCode === 13) {
        findItems();        
    }
}

function showUser() {
	var string = "Prijavljen kot: ";
	document.getElementById('prijavljen').innerHTML = string + document.getElementById("user_ime").value;
	document.getElementById('prijavljen').display = true;
}

function findItems() {
	var array = document.getElementsByTagName("h3");
	var find = document.getElementById("search").value;
	for(var i=0; i<array.length; i++) {
		if(find === array[i].childNodes[0].textContent || 
			find === array[i].childNodes[0].textContent.toUpperCase() ||
				find === array[i].childNodes[0].textContent.toLowerCase()) {
			array[i].parentElement.parentElement.style.backgroundColor = "lightblue";
		}
	}
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
	img.src = "iphone6.jpg";
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

function dodajTemo() {
	document.getElementById("naslovTeme").style.visibility = "visible";
	document.getElementById("ustvariTemo").style.visibility = "visible";
	document.getElementById("naslovTeme").style.marginBottom = "10px";
	document.getElementById("ustvariTemo").style.marginBottom = "10px";
}

function ustvari() {
	var t = document.createElement("h3");
	var text = document.getElementById("naslovTeme").value;
	var x = document.createTextNode(text);
	t.appendChild(x);
	t.style.textDecoration = "underline";
	var koren = document.getElementById("forumPage");
	koren.appendChild(t);
	t.style.padding = "0 0 0px 20px";
	t.style.border = "2px solid #73AD21";
	t.style.borderRadius = "25px";
	document.getElementById("naslovTeme").style.visibility = "hidden";
	document.getElementById("ustvariTemo").style.visibility = "hidden";
}

function showTextArea() {
	document.getElementById("forumOdgovor").style.visibility = "visible";
	document.getElementById("odgovoriA").style.visibility = "hidden";
}

function prikaziOdgovor(count) {
	var parentDiv = document.getElementsByClassName("vprasanja")[count];
	var p = document.createElement("p");
	var ptext = document.getElementById("textarea").value;
	var x = document.createTextNode(ptext);
	if(!ptext.length == 0) {	
		p.appendChild(x);
		parentDiv.append(p);
		//console.log(parentDiv);
		p.style.padding = "10px 30px 10px";
		p.style.border = "2px solid blue";
		p.style.borderRadius = "25px";
	}
	document.getElementById("forumOdgovor").style.visibility = "hidden";
	document.getElementById("odgovoriA").style.visibility = "visible";
	//var b = document.createElement("button");
	//b.id = "odgovoriA";
	//p.appendChild(b);
}

function preklic() {
	document.getElementById("forumOdgovor").style.visibility = "hidden";
	document.getElementById("odgovoriA").style.visibility = "visible";
}