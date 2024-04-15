function couleursGrille(x, y) {
    var grille = [];
    for (let lig = x[0]; lig <= x[1]; lig++) {
        for (let col = y[0]; col <= y[1]; col++) {
            let id = lig + ',' + col;
            let element = document.getElementById(id);
            if (element) {
                let couleur = element.style.backgroundColor;
                grille.push(`${id}:${couleur}`);
            }
        }
    }
    return grille;
}

var x = [90,119];
var y = [90,119];
couleursGrille(x, y);