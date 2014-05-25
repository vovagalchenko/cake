function highlight(text)
{
	return ' <span class = "cake-highlight">' + text + '</span> ';
}

var taglines = ['puts the' + highlight('finance') + 'in financier',
		'takes the' + highlight('moron') + 'out of macaroon',
		'takes the' + highlight('ugh') + 'out of dough',
		'puts the' + highlight('profit') + 'in profiterole',
		'puts the' + highlight('ease') + 'in measure',
		'takes the' + highlight('pain') + 'out of pain au chocolat'];


function pickTagline()
{
	var taglineElements = document.getElementsByClassName("tagline");
	var randomTagline = taglines[Math.floor(Math.random()*taglines.length)].toLowerCase();
	var formattedTagline = randomTagline.charAt(0).toUpperCase() + randomTagline.slice(1) + '.';
	taglineElements[0].innerHTML = formattedTagline;
}

pickTagline();
